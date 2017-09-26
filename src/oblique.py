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
def stable_x(ρ, w, k, l, x0=0.5, n=1000000):
    wA = cycle([1.0]*k + [w]*l)
    wB = cycle([w]*k + [1.0]*l)

    x = np.array([x0, 1-x0, 0.0, 0.0]) # no invader!
    x_prev = -1 * np.ones_like(x)
    t = 0 # for numba
    for t, wA_, wB_ in zip(count(1), wA, wB):
        x = modifier_recursion(x, wA=wA_, wB=wB_, ρ=ρ, P=0)
        if t % (k + l) == 0:
            if t > 1000 and np.allclose(x, x_prev):
                break
            x_prev = x.copy()
        if t == n:
            print("Reached iteration limit for ρ={}, w={}, k={}, l={}".format(ρ, w, k, l))
            break    
    return x

@numba.jit()
def simulation(ρ, w, k, l, x0=0.5, n=1000000):
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


@numba.jit()
def _simulation(ρ, w, k, l, x0=0.5, n=10000):
    wA = np.array(([1]*k + [w]*l) * n, dtype=float)
    wB = np.array(([w]*k + [1]*l) * n, dtype=float)
    
    ρ = np.array(ρ, ndmin=1)
    x = np.empty((wA.size, ρ.size))
    x_prev = np.empty((k+l, ρ.size))
    x[0, :] = x0
    x_prev[:, :] = -1
    t = 0 # for numba
    for t in range(1, n * (k + l)):
        x[t, :] = recurrence(x[t - 1, :], ρ=ρ, wA=wA[t], wB=wB[t])
        if t > (k+l)*3 and t % (k + l) == 0:
            if np.allclose(x[(t-k-l-1):t-1, :], x_prev, rtol=0, atol=1e-7):
                break
            x_prev = x[(t-k-l-1):t-1, :]
    assert (x_prev >= 0).all(), 'ρ={}, w={}, k={}, l={}, x[x<0]={}'.format(ρ, w, k, l, x_prev)
    assert (x_prev <= 1).all(), 'ρ={}, w={}, k={}, l={}, x[x>1]={}'.format(ρ, w, k, l, x_prev)
    if t >= n * (k + l) - 1:
        print("Reached iteration limit for ρ={}, w={}, k={}, l={}".format(ρ, w, k, l))
    return x_prev


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
    x = simulation(ρ, w, k, l)
    return -geom_avg_wbar(x, w, k ,l)[0]


@numba.jit()
def modifier_recursion(x, wA, wB, ρ, P, N=0, err=1e-14):
    x1, x2, x3, x4 = x
    x1_ = x1 * wA * ((1 - ρ) * (x1 + x3) + ρ) + x2 * wB * (1 - ρ) * (x1 + x3)
    x2_ = x1 * wA * (1 - ρ) * (x2 + x4) + x2 * wB * ((1 - ρ) * (x2 + x4) + ρ)
    x3_ = x3 * wA * ((1 - P) * (x1 + x3) + P) + x4 * wB * (1 - P) * (x1 + x3)
    x4_ = x3 * wA * (1 - P) * (x2 + x4) + x4 * wB * ((1 - P) * (x2 + x4) + P)
    x = x1_, x2_, x3_, x4_
    x = np.array(x)
    x /= x.sum()
    x[(x < err) & (x != 0)] = err
    x[(x > 1 - err) & (x != 1)] = 1 - err
    if N > 0:
        x = np.random.multinomial(N, x) / N
    return x


@numba.jit()
def invasion(x1, w, ρ, P, k, l, n=5000, inv_rate=1e-4):
    wA = cycle([1.0] * k + [w] * l)
    wB = cycle([w] * k + [1.0] * l)
    
    n -= n % (k + l)
    assert n % (k + l) == 0
    x = np.array(
        [x1*(1-inv_rate), (1-x1)*(1-inv_rate), x1*inv_rate, (1-x1)*inv_rate]
    )
    assert np.isclose(x.sum(), 1), x
    
    for t, wA_, wB_ in zip(range(n), wA, wB):
        x = modifier_recursion(x, wA=wA_, wB=wB_, ρ=ρ, P=P)
    if (x[2] + x[3]) > inv_rate:
        return P
    else:
        return ρ


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


def draw_ρ(w, k, l, ρ=None):
    if ρ is None:
        for _ in range(100):
            ρ = np.random.rand()
            if is_polymorphism(w, ρ, k, l):
                return ρ
        return np.nan
    else:
        for _ in range(100):
            if ρ > 0:
                P = min(max(ρ * np.random.exponential(1), 0), 1)
            elif ρ == 0:
                P = min(max(np.random.exponential(0.1), 0), 1)
            if np.isclose(P, 0.0):
                return 0.0
            if np.isclose(P, 1.0):
                return 1.0
            if is_polymorphism(w, P, k, l):
                return P
        return ρ


def evol_stable(w, k, l=None, reps=1, PRINT=False):
    if l is None:
        l = k    
    
    results = []
    for i in range(reps):
        ρ = draw_ρ(w, k, l)
        if PRINT:
            print('ρ(0)={:2g}'.format(ρ))
        if np.isnan(ρ):
            print("No ρ allows polymorphism with w={}, k={}, l={}".format(w, k, l))
            return ρ
        x0 = stable_x(ρ, w, k, l)[0]
        P = -1 # for numba
        failed_invasions = 0
        invasions = 0
        while True:
            P = draw_ρ(w, k, l, ρ=ρ)
            if PRINT:
                print('P({})={:.2g}'.format(failed_invasions, P), end=', ')
                sys.stdout.flush()
            P = invasion(x0, w, ρ, P, k, l)
            invasions += 1
            if P == ρ:
                failed_invasions += 1
            else:
                failed_invasions = 0
                ρ = P
                x0 = stable_x(ρ, w, k, l, x0=x0)[0]
                if PRINT:
                    print('ρ({})={:.2g}'.format(invasions, ρ))
                    sys.stdout.flush()
            if failed_invasions >= 50 and invasions >= 500:
                break            
        # if ρ is almost 0 or almost 1, try to invade with 0 or 1.
        if ρ < 1e-3:
            x0 = stable_x(ρ, w, k, l, x0=x0)[0]
            ρ = invasion(x0, w, ρ, 0.0, k, l)
        elif ρ > 1 - 1e-3:
            x0 = stable_x(ρ, w, k, l, x0=x0)[0]
            ρ = invasion(x0, w, ρ, 1.0, k, l)
        if PRINT:
            print('ρ: {:.2g} ({})'.format(ρ, invasions))
        results.append(ρ)
    if PRINT:
        print(results)
    ρ = results.pop()    
    while results:
        P = results.pop()
        x0 = stable_x(ρ, w, k, l)[0]
        if P == ρ: continue
        if invasion(x0, w, ρ, P, k, l, inv_rate=0.5) == P:
            if PRINT:
                print('P={:.2g} takes over ρ={:.2g}'.format(P, ρ))
            ρ = P
            x0 = stable_x(ρ, w, k, l, x0=x0)[0]
    return ρ
