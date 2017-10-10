import numba
import numpy as np
import pandas as pd
import scipy.stats
import scipy.optimize
from itertools import cycle, count
import sys

@numba.jit()
def recurrence(x, ρ, wA, wB, N=0, err=1e-14):
    N = int(N)
    wbar = x * wA + (1 - x) * wB
    # same precision around x=0 and x=1
    if np.all(x > 0.5): 
        x = 1 - (ρ * (1 - x) * wB/wbar + (1 - ρ) * (1 - x))
    else:
        x = ρ * x * wA/wbar + (1 - ρ) * x
    # move from edges to get out of non-stable equilibriums at x=0 and x=1
    if hasattr(x, 'size') and x.size > 1:
        x[x < err ] = err
        x[x > 1 - err] = 1 - err
    else:
        if x < err:
            x = err
        elif x > 1 - err:
            x = 1 - err
    if N > 0:
        x = np.random.binomial(N, x) / N
    return x


@numba.jit()
def stable_x_target(x0, ρ, w, k, l):
    wA = [1.0]*k + [w]*l
    wB = [w]*k + [1.0]*l
    x = np.array([x0, 1-x0, 0.0, 0.0])
    for wA_, wB_ in zip(wA, wB):
        x = modifier_recursion(x, wA=wA_, wB=wB_, ρ=ρ, P=0)
    return abs(x[0] - x0)

def stable_x(ρ, w, k, l, x0=0.5):
    res = scipy.optimize.minimize_scalar(
        stable_x_target, x0, args=(ρ, w, k, l), 
        bounds=[0,1], method="bounded"
    )
    assert res.success, res
    return res.x


@numba.jit()
def stable_cycle(ρ, w, k, l, x0=0.5, n=1000000):
    wA = cycle([1.0]*k + [w]*l)
    wB = cycle([w]*k + [1.0]*l)
    
    ρ = np.array(ρ, ndmin=1)
    x = np.zeros((k+l, ρ.size))
    x_prev = -1 * np.ones((k+l, ρ.size))
    x[0, :] = x0
    t = 0 # for numba
    for t, wA_, wB_ in zip(count(1), wA, wB):
        x[t%(k+l), :] = recurrence(x[(t-1)%(k+l), :], ρ=ρ, wA=wA_, wB=wB_)
        if t % (k + l) == 0:
            if t > 1000 and np.allclose(x, x_prev, rtol=0, atol=1e-5):
                break
            x_prev = x.copy()           
            if t == n:
                print("Reached iteration limit for ρ={}, w={}, k={}, l={}".format(ρ, w, k, l))
                break
    assert (x >= 0).all(), 'ρ={}, w={}, k={}, l={}, x={}'.format(ρ, w, k, l, x)
    assert (x <= 1).all(), 'ρ={}, w={}, k={}, l={}, x={}'.format(ρ, w, k, l, x)
    return x


def geom_avg_wbar(x, w, k, l):
    x = x[-k-l:]
    wA = np.array([1]*k + [w]*l, dtype=float).reshape((k+l, 1))
    wB = np.array([w]*k + [1]*l, dtype=float).reshape((k+l, 1))
    wbars = x * wA + (1 - x) * wB
    assert (wbars > 0).all(), wbars
    res = scipy.stats.mstats.gmean(wbars)
    assert (0 < res).all(), (res, k, l)
    assert (res < 1).all(), (res, k, l)
    return res


def geom_wbar_target(ρ, w, k, l):
    x = stable_cycle(ρ, w, k, l)
    return -geom_avg_wbar(x, w, k ,l)[0]


def optimal_ρ(w, k, l):    
    max_ρ = max_ρ_with_polymorphism(w, k, l)
    if np.isclose(max_ρ, 0):
        return np.nan
    res = scipy.optimize.minimize_scalar(
        geom_wbar_target, args=(w, k, l), bounds=[0, max_ρ], method='bounded')
    if not res.success: 
        print('Minimization failed for w={}, k={}, l={}'.format(w, k, l))
        return np.nan
    return res.x


def is_polymorphism(w, ρ, k, l):
    # see eq 22
    s = 1 - w
    if ρ*s == 0:
        return True
    elif k == l:
        return True
    elif l > k:
        return l/k < -np.log(1+ρ*s/(1-s))/np.log(1-ρ*s) 
    else: # k > l
        return k/l < -np.log(1+ρ*s/(1-s))/np.log(1-ρ*s) 


def max_ρ_with_polymorphism(w, k, l, num_pts=1001):
    for ρ_ in np.linspace(0, 1, num_pts)[::-1]:
        if is_polymorphism(w, ρ_, k, l): 
            return ρ_


if __name__ == '__main__':
    ks = np.arange(1, 51, 1, dtype=int)
    ws = np.array([0.1, 0.5, 0.9])

    ρs = np.empty((ws.size, ks.size))
    for i, w in enumerate(ws):
        for j, k in enumerate(ks):
            print("w={}, k={}, l={}".format(w, k, k))
            ρs[i, j] = optimal_ρ(w, k, k)
            print("ρ={}".format(ρs[i, j]))
    fname = 'optimal_ρ_{}.npz'.format(uuid().hex)
    np.savez_compressed(fname, ks=ks, ws=ws, ρs=ρs)
