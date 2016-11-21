# -*- coding: utf-8 -*-
"""
TODO

Created on Thu Nov 17 16:24:45 2016

@author: yoav@yoavram.com
"""
import datetime
import os
import gzip
import json
import warnings
# filter seaborn nasty warning
warnings.filterwarnings('ignore', 'The `IPython.html` package has been deprecated. You should import from `notebook` instead. `IPython.html.widgets` has moved to `ipywidgets`.')

import click
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

__version__ = '0.0.1'
output_folder = 'output'
sns.set(style='ticks', context='paper', font_scale=1.3)

def simulation(N, n, η, μ, ω0, ω1, π0, ϵ=None):
    """Run a single simulation.
    
    Parameters
    ----------
    N : int
        constant population size
    n : int
        number of generations
    η : float
        learning rate, 0 <= η <= 1
    μ : float
        mutation rate, 0 <= μ <= 1
    ω0, ω1 : float
        two fitness values for the two phenotyes in the two environments, ω > 0
    π0 : float
        initial value for π
    ϵ : numpy.ndarray
        ϵ[t] is the environment at time t
    """
    ω = np.array(
        [
            [ω0, ω1],
            [ω1, ω0]
        ],
    dtype=float)
    
    if ϵ is None:
        ϵ = np.random.randint(0, 2, n)
    # π[t, i] is the probability for phenotype 0 at individual i at time t
    π = np.zeros((n, N), dtype=float)
    π[0, :] = np.random.normal(π0, np.sqrt(π0 / 10), N)
    π[0, π[0, :] < 0] = 0
    π[0, π[0, :] > 1] = 1

    for t in range(n - 1):
        # phenotype of each individual
        φ = np.zeros(N, dtype=int)
        φ[np.random.random(N) > π[t, :]] = 1
        # fitness of each invidividual in current environment
        ω_t = ω[ϵ[t], φ]
        ω_t = ω_t / ω_t.sum()
        # selection & reproduction; idx is the indexes of reproducing individuals
        idx = np.random.choice(N, N, True, ω_t)
        # offspring phenotype probability
        μ_ = μ * np.random.choice((-1, 1), N, True)
        π[t + 1, :] = (1 - η) * π[t, idx] + η * (φ[idx] == 0) + μ_ 
        
    return π


def plot_π(π, ϵ, ax=None):    
    if ax is None:
        fig, ax = plt.subplots()
    for i in range(8):
        low, high = np.percentile(π, [0.5*(2**i), 100-0.5*(2**i)], 1)
        ax.fill_between(range(π.shape[0]), low, high, color='b', alpha=0.1)
    ax.plot(π.mean(axis=1), c='y', lw=3)
    ax.axhline((ϵ==0).mean(), color='k')
    ax.set(
        ylim=(0, 1),
        ylabel='$π_A$',
        xlabel='t'
    )
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


def simulation_modifiers(N, n, η1, η2, μ1, μ2, ω0, ω1, π0, ϵ=None):
    """Run a single simulation.
    
    Parameters
    ----------
    N : int
        constant population size
    n : int
        number of generations
    η1, η2 : float
        learning rate, 0 <= η <= 1
    μ1, μ2 : float
        mutation rate, 0 <= μ <= 1
    ω0, ω1 : float
        two fitness values for the two phenotyes in the two environments, ω > 0
    π0 : float
        initial value for π
    ϵ : numpy.ndarray
        ϵ[t] is the environment at time t
    """
    ω = np.array(
        [
            [ω0, ω1],
            [ω1, ω0]
        ],
    dtype=float)
    
    if ϵ is None:
        ϵ = np.random.randint(0, 2, n)
    # π[t, i] is the probability for phenotype 0 at individual i at time t
    π = np.zeros((n, N), dtype=float)
    π[0, :] = np.random.normal(π0, np.sqrt(π0 / 10), N)
    π[0, π[0, :] < 0] = 0
    π[0, π[0, :] > 1] = 1
    # η[t, i] is the learning rate for individual i
    η = np.empty(N, dtype=float)
    η[:N//2] = η1
    η[N//2:] = η2
    η_bar = np.empty(n, dtype=float)
    η_bar[0] = η.mean()
    # μ[t, i] is the mutation rate for individual i
    μ = np.empty(N, dtype=float)
    μ[:N//2] = μ1
    μ[N//2:] = μ2
    μ_bar = np.empty(n, dtype=float)
    μ_bar[0] = η.mean()
    
    for t in range(n - 1):
        # phenotype of each individual
        φ = np.zeros(N, dtype=int)
        φ[np.random.random(N) > π[t, :]] = 1
        # fitness of each invidividual in current environment
        ω_t = ω[ϵ[t], φ]
        ω_t = ω_t / ω_t.sum()
        # selection & reproduction; idx is the indexes of reproducing individuals
        idx = np.random.choice(N, N, True, ω_t)
        # offspring phenotype probability
        η = η[idx]
        η_bar[t + 1] = η.mean()
        μ = μ[idx]
        μ_bar[t + 1] = μ.mean()
        μ_ = μ * np.random.choice((-1, 1), N, True)
        π[t + 1, :] = (1 - η) * π[t, idx] + η * (φ[idx] == 0) + μ_
    
    return π, η_bar, μ_bar


def plot_η(η_bar, η1, η2, ax=None):    
    if ax is None:
        fig, ax = plt.subplots()
    ax.plot(η_bar)
    ax.axhline(η1, color='k', ls='--')
    ax.axhline(η2, color='k', ls='--')
    ax.set(
        xlabel='t',
        ylabel=r'$\bar{\eta}$',
        ylim=(0.9 * η1, η2 * 1.1),
    )

    ax.set_clip_on(False)
    sns.despine()
    return ax

def write_json(filename, data):
    filename = os.path.join(output_folder, '{}_{}.json'.format('params', filename))
    click.echo("Writing parameters to {}".format(filename))
    with open(filename, 'wt') as f:
        json.dump(data, f)

def write_csv_gz(filename, prefix, data):
    filename = os.path.join(output_folder, '{}_{}.csv.gz'.format(prefix, filename))
    click.echo("Writing {} to {}".format(prefix, filename))
    with gzip.open(filename, 'w') as f:
        np.savetxt(f, data, delimiter=', ')


@click.command()
@click.version_option(version=__version__, prog_name=__name__)
@click.option('--Ne', type=int, help="Population size")
@click.option('--n', default=10, help="Number of generations")
@click.option('--η1', default=0.1, help="Learning rate")
@click.option('--η2', default=None, help="Invader modifier learning rate")
@click.option('--μ1', default=0.0, help="Mutation rate")
@click.option('--μ2', default=None, type=float, help="Invader modifier mutation rate")
@click.option('--ω0', default=2.0, help="Fitness of phenotype 0 in environment 0")
@click.option('--ω1', default=0.0, help="Fitness of phenotype 0 in environment 1")
@click.option('--π0', default=0.5, help="Initial probability of phenotype 0")
@click.option('--env', default='A', type=click.Choice('A B C'.split()), help="Type of environment, corresponding to Fig. 2")
def main(ne=100, n=100, η1=0.1, η2=None, μ1=0, μ2=None, ω0=2.0, ω1=0.2, π0=0.5, env='A'):
    N = ne
    now = datetime.datetime.now()
    params = dict(N=N, n=n, η1=η1, η2=η2, μ1=μ1, μ2=μ2, ω0=ω0, ω1=ω1, π0=π0, env=env)
    click.echo("Starting simulation {} with parameters:\n{!r}".format(now, params))

    if env == 'A':
        ϵ = np.random.choice(2, n, True, [0.7, 0.3])
    elif env == 'B':
        ϵ, a = np.zeros(n, dtype=int), 0
        while a < ϵ.size:
            a += np.random.geometric(1/10)
            g = np.random.geometric(1/5)
            ϵ[a: a + g] = 1
            a += g
    elif env == 'C':
        ϵ = np.array(([0] * 40 + [1] * 40) * (n//80 + 1))
        ϵ = ϵ[:n]
    else:
        raise ValueError("Unknown value for env: {}".format(env))

    if η2 is None and μ2 is None:
        π = simulation(N, n, η1, μ1, ω0, ω1, π0, ϵ)
    else:
        if μ2 is None:
            μ2 = μ1
        if η2 is None:
            η2 = η1
        π, η_bar, μ_bar = simulation_modifiers(N, n, η1, η2, μ1, μ2, ω0, ω1, π0, ϵ)

    filename = now.isoformat().replace(':', '-')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    write_json(filename, params)
    write_csv_gz(filename, 'π', π.mean(axis=1))
    write_csv_gz(filename, 'ϵ', ϵ)    
    if η2 is not None and η2 != η1:
        write_csv_gz(filename, 'η', η_bar)
    if μ2 is not None and μ2 != μ1:
        write_csv_gz(filename, 'μ', μ_bar)

if __name__ == '__main__':
    main()