#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of a repo located at
# https://github.com/yoavram/Milpitas
# which supports the manuscript:
# Vertical and Oblique Transmission under Fluctuating Selection
# by Yoav Ram, Uri Liberman, & Marcus W. Feldman.

# The file includes functions used to calculate the vertical transmission rate
# that maximized the geometric average of the population mean fitness under fluctuating selection.

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Yoav Ram <yoav@yoavram.com>
import sys
from itertools import cycle, count
from uuid import uuid4 as uuid

import numpy as np
import scipy.stats
import scipy.optimize
import numba


@numba.jit()
def recurrence(x, ρ, wA, wB, N=0, err=1e-14):
    """Calculate the frequency of phenotype A in the next generation.

    Parameters
    ----------
    x : float or np.ndarray with dtype=float
        current frequency of phenotype A
    ρ : float or np.ndarray with dtype=float
        vertical transmission rate
    wA, wB : float
        fitness of phenotype A and B
    N : int
        population size (0 means 'infinite populatio')
    err : float
        x will be maintained in the segment [err, 1-err] so that it doesn't hit 0 or 1

    Returns
    -------
    x : float or np.ndarray with dtype=float
        the frequency of phenotype A in the next generation.
    """
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
        geom_wbar_target, args=(w, k, l), 
        bounds=[0, max_ρ], method='bounded')
    if not res.success: 
        print('Minimization failed for w={}, k={}, l={}'.format(w, k, l))
        return np.nan
    # check that we didn't get stuck in local max or plateau
    # this occurs, for example, with w=0.5, k=l=25 and w=0.1 k=l=10
    if geom_wbar_target(1e-10, w, k, l) < res.fun:
        return 0.0
    else:
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
    w = float(sys.argv[1])
    ks = np.arange(1, 51, 1, dtype=int)    

    optimal_rates = []
    for j, k in enumerate(ks):
        print("w={}, k={}, l={}".format(w, k, k))
        optimal_rates.append( optimal_ρ(w, k, k) )
        print("ρ={}".format(optimal_rates[-1]))
    optimal_rates = np.array(optimal_rates)

    fname = 'optimal_rates_w_{}_{}.npz'.format(w, uuid().hex)
    np.savez_compressed(fname, ks=ks, optimal_rates=optimal_rates)
