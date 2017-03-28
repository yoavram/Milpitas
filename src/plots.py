# -*- coding: utf-8 -*-
"""
TODO

Created on Sun Jan 08 10:43:42 2017

@author: yoav@yoavram.com
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from simulation import simulation, parse_env, parse_π0


def plot_π(π, ϵ=None, bands=8, label=None, ax=None):    
    if ax is None:
        fig, ax = plt.subplots()
    for i in range(bands):
        low, high = np.percentile(π, [0.5*(2**i), 100-0.5*(2**i)], 1)
        ax.fill_between(range(π.shape[0]), low, high, color='b', alpha=0.1)
    ax.plot(π.mean(axis=1), c='y', lw=3)
    if ϵ is not None:
        ax.axhline((ϵ == 0).mean(), color='k', ls='--')
    ax.set(
        ylim=(0, 1),
        ylabel='$π$',
        xlabel='t'
    )
    if label is not None:
        ax.set_label(label)
    ax.set_clip_on(False)
    sns.despine()
    return ax

def plot_logNtN0(π, ω0, ω1, p0, ϵ, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    
    # estimated log(Nt/N0)
    ω = np.array(
        [
            [ω0, ω1],
            [ω1, ω0]
        ],
    dtype=float)
    π_bar = π.mean(axis=1)
    Δ = np.log(π_bar * ω[ϵ, 0] + (1 - π_bar) * ω[ϵ, 1]) # eq. 17
    logNtN0 = Δ.cumsum() # eq. 18
    ax.plot(logNtN0, 'b')
    # max possible log(Nt/N0)
    maxlogNtN0 = np.repeat(np.log(ω0), logNtN0.size).cumsum()
    ax.plot(maxlogNtN0, 'y') 
    # bet-hedging  log(Nt/N0), eq. 11
    ax.plot(np.repeat(
        p0 * np.log(p0 * ω0 + (1 - p0) * ω1) + (1 - p0) * np.log(p0 * ω1 + (1 - p0) * ω0),
        logNtN0.size
    ).cumsum(), 'k')

    ax.set(
        xlabel='t',
        ylabel='$log(N_t/N_0)$',
        yticks=np.arange(0, maxlogNtN0.max(), 20)
    )
    ax.set_clip_on(False)
    sns.despine()
    return ax

def plot_η(η_bar, η1, η2, ax=None):    
    if ax is None:
        fig, ax = plt.subplots()
    ax.plot(η_bar)
    ax.axhline(η1, color='k', ls='--')
    ax.axhline(η2, color='k', ls='--')
    ηm, ηM = η1, η2
    if ηm == 0 and ηM == 0:
        ηm, ηM = 0, 0.1
    if ηm > ηM:
        ηm, ηM = ηM, ηm
    ηm, ηM = ηm * 0.9, ηM * 1.1
    ax.set(
        xlabel='t',
        ylabel=r'$\bar{\eta}$',
        ylim=(ηm, ηM),
    )

    ax.set_clip_on(False)
    sns.despine()
    return ax

def plot_μ(μ_bar, μ1, μ2, ax=None):
    ax = plot_η(μ_bar, μ1, μ2, ax=ax)   
    ax.set(
        ylabel=r'$\bar{\mu}$',
    )
    return ax

def plot_simulations(df, samples=10):
    fig, ax = plt.subplots(3, 3, sharex='col', sharey='row', figsize=(12,6))
    red, green, blue = sns.color_palette('Set1', 3)
    for i, env in enumerate(('A', 'B', 'C')):
        _df = df[df.env == env]
        ids = np.random.choice(_df.ID.unique(), samples)
        grp = _df[_df.ID.isin(ids)].groupby('ID')
        sns.tsplot(_df, time='t', unit='ID', value='π', lw=2, color=blue, ci=False, ax=ax[0, i])
        grp.plot('t', 'π', color=blue, alpha=2/samples, ax=ax[0, i])
        if 'η' in df.columns:
            sns.tsplot(_df, time='t', unit='ID', value='η', lw=2, color=green, ci=False, ax=ax[1, i])
            grp.plot('t', 'η', color=green, alpha=2/samples, ax=ax[1, i])
        if 'μ' in df.columns:
            sns.tsplot(_df, time='t', unit='ID', value='μ', lw=2, color=red, ci=False, ax=ax[2, i])
            grp.plot('t', 'μ', color=red, alpha=0.02, ax=ax[2, i])
        ax[0, i].axhline(_df.ϵ.mean(), color='k', ls='--')
        for j in range(3):
            lg = ax[j, i].legend()
            if lg: lg.set_visible(False)

    sns.despine()
    return ax


def plot_π_deterministic(π, f, ϵ, N, only_mean=False, color='y', label=None, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    n = len(f)
    m = [0] * n

    for t, π_, f_ in zip(range(n), π, f):
        l = []
        for x, p in zip(π_, f_):
            if not only_mean:
                l += [x] * int(p*N)
            m[t] += x * p
        if not only_mean:
            ax.plot([t] * len(l), l, '.b', alpha=0.005)

    ax.plot(range(n), m, c=color, label=label, lw=2)
    ax.axhline((ϵ == 0).mean(), color='k', ls='--')
    ax.set(
        ylim=(0, 1),
        ylabel='$π$',
        xlabel='t'
    )
    ax.set_clip_on(False)
    sns.despine()
    return ax

def plot_simulation_k_l(π0, env, period, N, n, η, ω0, ω1, 
                        nbins=101, ax=None, save=False, title=True):
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure
    ϵ = parse_env(env, n)
    π = simulation(N=N, n=n, η=η, μ=0, ω0=ω0, ω1=ω1, 
                   ϵ=ϵ, π0=parse_π0(π0))
    π = π[::period]
    ϵ = ϵ[::period]

    bins = np.linspace(0, 1, nbins)
    freq = np.array([
        np.histogram(π[t,:], bins=bins)[0] 
        for t in range(n//period)
    ])
    aspect = freq.shape[0]/freq.shape[1]
    im = ax.imshow(freq.T, aspect=aspect, cmap='viridis', 
                   origin=(0,0), vmin=0, vmax=N//(nbins//10))
    if title:
        ax.set_title('{}, π0={}\nη={}, ω0={}, ω1={}'.format(env, π0, η, ω0, ω1))
    ax.set(
        ylabel='$\pi$',
        yticks=np.linspace(0, nbins, 6, dtype=int),
        yticklabels=map(
            lambda x: round(x, 2),
            bins[np.linspace(0, nbins, 6, dtype=int)[:-1]].tolist() + [1]
        ),
        xlabel='Periods (τ={:d})'.format(period)
    )
    sns.despine()
    if save: 
        fig.savefig('../figures/{}_π0_{}_η_{}_ω0_{}_ω1_{}.png'.format(
            env, π0, η, ω0, ω1
        ))
    return π, freq, ax