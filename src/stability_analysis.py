import sys
from uuid import uuid4 as uuid
from concurrent.futures import ProcessPoolExecutor as Executor
from concurrent.futures import wait
from functools import lru_cache
import warnings

import autograd.numpy as np
from autograd import grad, jacobian
from scipy import optimize as opt


def f1(x, wA, wB, ρ, dx=0):    
    wbar = x * wA + (1 - x) * wB
    x = ρ * x * wA/wbar + (1 - ρ) * x
    if dx > 0:
        x += dx * np.sign(wB - wA)
    return x
df1 = grad(f1)

def test_f1():
    W, w = 1.0, 0.5
    ρ = 0.5
    x = 0.25
    dx = 1e-4
    assert np.isclose(
        f1(x + dx, W, w, ρ, dx=1e-10), 
        f1(x, W, w, ρ, dx=1e-10) + df1(x, W, w, ρ, dx=1e-10) * dx
    )


def F1(x, W, w, ρ, k, l, dx=0): 
    for _ in range(k):
        x = f1(x, W, w, ρ, dx=dx)
    for _ in range(l):
        x = f1(x, w, W, ρ, dx=dx)
    return x
dF1 = jacobian(F1)

def test_F1():
    W, w = 1.0, 0.5
    ρ = 0.5
    x = 0.25
    dx = 1e-4
    assert np.isclose(
        F1(x + dx, W, w, ρ, 1, 1, dx=1e-10), 
        F1(x, W, w, ρ, 1, 1, dx=1e-10) + dF1(x, W, w, ρ, 1, 1, dx=1e-10) * dx
    )

def stablex1(W, w, ρ, k, l, x0=0.5, dx=0):
    x = x0
    x_prev = -1
    while not np.isclose(x, x_prev):
        x, x_prev = F1(x, W, w, ρ, k, l, dx=dx), x
#     assert np.isclose(F1(x, W, w, ρ, k, l, dx=dx), x)
    return x

lru_cache()
def test_stablex1():
    W, w = 1.0, 0.5
    ρ = 0.5
    k, l = 1, 1
    x = stablex1(W, w, ρ, k, l, dx=1e-8)
    assert np.isclose(x, F1(x, W, w, ρ, k, l, dx=1e-8))


A = np.array([1.0, 0.0, 1.0, 0.0])
B = np.array([0.0, 1.0, 0.0, 1.0])

def Tf2(x, wA, wB, ρ, P):
    S = A * wA + B * wB
    xA = A @ x
    xB = B @ x
    wbar = S @ x
    S = np.diag(S) / wbar

    Q = np.array(
        [[xA, xA, 0, 0],
         [xB, xB, 0, 0],
         [0, 0, xA, xA],
         [0, 0, xB, xB]])
    r = np.array([ρ, ρ, P, P])
    R = Q @ np.diag(1-r) + np.diag(r)
    assert np.allclose(R.sum(axis=0), 1), R.sum(axis=1)
    
    return R @ S


def f2(x, wA, wB, ρ, P, dx=0):
    x = Tf2(x, wA, wB, ρ, P) @ x
    if dx > 0:
        dv = dx * np.array([wB-wA, wA-wB, wB-wA, wA-wB])
        x += dv
    return x
df2 = jacobian(f2)

def test_f2():
    W, w = 1.0, 0.5
    ρ = 0.5
    x = np.array([0.7, 0.3, 0.0, 0.0])
    dx = np.array([0.001, -0.001, 0, 0])
    assert np.allclose(
        f2(x+dx, W, w, ρ, P, dx=1e-10), 
        f2(x, W, w, ρ, P, dx=1e-10) + df2(x, W, w, ρ, P, dx=1e-10) @ dx
    )


def F2(x, W, w, ρ, P, k, l, dx=0): 
    for _ in range(k):
        x = f2(x, W, w, ρ, P, dx)
    for _ in range(l):
        x = f2(x, w, W, ρ, P, dx)
    return x
dF2 = jacobian(F2)


def test_F2():
    W, w = 1.0, 0.5
    ρ = 0.5
    k, l = 1, 1
    dx = np.array([-1e-6, -1e-6, 1e-6, 1e-6])
    assert np.allclose(
        F2(x+2*dx, W, w, ρ, P, k, l), 
        F2(x+dx, W, w, ρ, P, k, l) + dF2(x+dx, W, w, ρ, P, k, l) @ dx
    )


def external_stability_matrix(W, w, ρ, P, k, l, dx=1e-8):
    args1 = (W, w, ρ, k, l)
    args2 = (W, w, ρ, P, k, l)
    x1 = stablex1(*args1)
    if not np.allclose(x1, F1(x1, *args1)):
        warnings.warn("Stable x without M wasn't so stable: {}->{}".format(x1, F1(x1, *args1)))
    x = np.array([x1, 1-x1, 0.0, 0.0])
    if not np.allclose(x, F2(x, *args2)):
        warnings.warn("Stable x without M wasn't stable with M: {}->{}".format(x, F2(x, *args2)))
    J = dF2(x, *args2, dx=dx)
    L = J[2:,2:]
    return L


def λ1(W, w, ρ, P, k, l, dx=1e-8):
    # np.linalg.eigvals not supported by autograd, using formula
    # the standard formula losses precision, using non-standard
    # see: https://en.wikipedia.org/wiki/Loss_of_significance#Instability_of_the_quadratic_equation
    L = external_stability_matrix(W, w, ρ, P, k, l, dx=dx)
    # L = | L11 L12 |
    #     | L21 L22 |
    L11, L12, L21, L22 = L.ravel()
    # a = 1
    b = -(L11 + L22)
    c = L11 * L22 - L12 * L21
    D = np.sqrt(b**2 - 4*c)
    x1 = (-b - np.sign(b) * D) / 2
    assert np.isreal(x1), x1
    x2 = c / x1
    assert np.isreal(x2), x2
    return np.maximum(x1, x2)
dλ1 = grad(λ1, 3)


def test_λ1():
    W, w = 1.0, 0.5
    k = l = 3    
    ρ, P = 0.5, 0.4
    Lex = external_stability_matrix(W, w, ρ, P, k, l, dx=1e-8)
    assert np.isclose(
        λ1(W, w, ρ, P, k, l, dx=1e-8), 
        np.linalg.eigvals(Lex).max()
    )


def vλ1(W, w, ρs, Ps, k, l):
    with Executor() as exe:
        futures = [[exe.submit(λ1, W, w, ρ, P, k, l) for P in Ps] for ρ in ρs]
    return np.array([[f.result() for f in fs] for fs in futures])


def vdλ1(W, w, ρs, Ps, k, l):
    return np.array([[dλ1(W, w, ρ, P, k, l) for P in Ps] for ρ in ρs])


def grad_ascent(W, w, k, l, ρ0=0.5, η=1e-2, 
                 η0=1e-4, η_factor=2, convergence_tol=1e-2, λ1_atol=1e-6):
    ρ = ρ0
    ρs = [-1, ρ]
    η_ = η
    while η > η0 and not np.isclose(ρs[-1], ρs[-2], atol=convergence_tol) and 0 < ρ < 1:
        P = ρ + η * dλ1(W, w, ρ, ρ, k, l)
        if λ1(W, w, ρ, P, k, l) > 1-λ1_atol:
            ρ = P
            ρs.append(ρ)
            η = η_
        else:
            η /= η_factor
    ρs.pop(0)
    if ρs[-1] < 0:
        ρs[-1] = 0
    elif ρs[-1] > 1:
        ρs[-1] = 1
    return ρs



def find_stable_rate(W, w, k, l):
    def λ1_(ρ, P):
        return λ1(W, w, ρ, P, k, l)
    dλ1dρ = grad(λ1_, 0)
    dλ1dP = grad(λ1_, 1)

    def target(ρ):
        return dλ1dP(ρ, ρ)
    
    if target(0.0) * target(1-1e-5) < 0:    
        ρ, res = opt.brentq(target, 0.0, 1-1e-5, full_output=True)        
        if res.converged and np.isclose(target(ρ), 0):
            return ρ
    elif dλ1dP(0.0, 0.0) <= 0:
        return 0.0
    return 1.0


if __name__ == '__main__':
    w = float(sys.argv[1])
    W = 1.0
    ks = np.arange(1, 2, 1, dtype=int)
    stable_rates = []

    for k in ks:
        stable_rates.append( find_stable_rate(W, w, k, k) )
    stable_rates = np.array(stable_rates)

    fname = 'stable_rates_w_{}_{}.npz'.format(w, uuid().hex)
    np.savez_compressed(fname, stable_rates=stable_rates, ks=ks)
