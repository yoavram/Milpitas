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
import glob
import re
import warnings
# filter seaborn nasty warning
warnings.filterwarnings('ignore', 'The `IPython.html` package has been deprecated. You should import from `notebook` instead. `IPython.html.widgets` has moved to `ipywidgets`.')

import click
import numpy as np
import pandas as pd
from ultrachronic import repeat

__version__ = '0.0.4'
env_pattern = re.compile("A(?P<k>\d+)B(?P<l>\d+)")

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
    π0 : function
        function that given N, returns an initial value for π.
    ϵ : numpy.ndarray
        ϵ[t] is the environment at time t

    Returns
    -------
    π : np.ndarray
        π[t, i] is the probability for phenotype 0 in individual i at time t
    """
    ω = np.array(
        [
            [ω0, ω1],
            [ω1, ω0]
        ],
    dtype=float)
    
    if ϵ is None:
        ϵ = np.random.randint(0, 2, n)
    # π[t, i] is the probability for phenotype 0 atin individual i at time t
    π = np.zeros((n, N), dtype=float)
    π[0, :] = π0(N)
    π[0, π[0, :] < 0] = 0
    π[0, π[0, :] > 1] = 1

    for t in range(n - 1):
        # phenotype of each individual
        φ = np.zeros(N, dtype=int)
        φ[np.random.random(N) > π[t, :]] = 1
        # fitness of each invidividual in current environment
        ω_t = ω[ϵ[t], φ]
        assert (ω_t > 0).any(), "Population extinct, ω_t=0"
        ω_t = ω_t / ω_t.sum()
        # selection & reproduction; idx is the indexes of reproducing individuals
        idx = np.random.choice(N, N, True, ω_t)
        # offspring phenotype probability
        π_ = π[t, idx]
        π_ = (1 - μ) * π_ + μ * np.random.randint(0, 2, π_.shape) # mutation
        π_ = (1 - η) * π_ + η * (φ[idx] == 0) # learning
        assert (π_ <= 1).all(), π_[π_ > 1]
        assert (π_ >= 0).all(), π_[π_ < 0]
        π[t + 1, :] = π_
    return π



def simulation_modifiers(N, n, η1, η2, μ1, μ2, ω0, ω1, π0, κ=0, ϵ=None):
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
    π0 : float or function
        initial value for π: if float then using Normal(π0, π0/10), if function then calling it with N.
    κ : float
        modifier mutation rate, 0 <= κ <= 1
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
    if isinstance(π0, (float, int)):
        π[0, :] = np.random.normal(π0, np.sqrt(π0 / 10), N)
    else:
        π[0, :] = π0(N)
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
        μ = μ[idx]
        if κ > 0:
            κ_idx = np.random.random(N) < κ
            η[κ_idx] = np.random.choice((η1, η2), κ_idx.sum(), True)
            κ_idx = np.random.random(N) < κ
            μ[κ_idx] = np.random.choice((μ1, μ2), κ_idx.sum(), True)            
        η_bar[t + 1] = η.mean()
        μ_bar[t + 1] = μ.mean()
        π_ = π[t, idx]
        π_ = (1 - μ) * π_ + μ * np.random.randint(0, 2, π_.shape) # mutation
        π_ = (1 - η) * π_ + η * (φ[idx] == 0) # learning
        assert (π_ <= 1).all(), π_[π_ > 1]
        assert (π_ >= 0).all(), π_[π_ < 0]
        π[t + 1, :] = π_

    return π, η_bar, μ_bar

def write_json(output_folder, filename, data):
    filename = os.path.join(output_folder, '{}_{}.json'.format('params', filename))
    click.echo("Writing parameters to {}".format(filename))
    with open(filename, 'wt') as f:
        json.dump(data, f)

def write_csv_gz(output_folder, filename, prefix, data):
    filename = os.path.join(output_folder, '{}_{}.csv.gz'.format(prefix, filename))
    click.echo("Writing {} to {}".format(prefix, filename))
    with gzip.open(filename, 'w') as f:
        np.savetxt(f, data, delimiter=', ')

def read_json(output_folder, filename):
    filename = os.path.join(output_folder, '{}_{}.json'.format('params', filename))
    with open(filename, 'r') as f:
        return json.load(f)

def read_csv_gz(output_folder, filename, prefix):
    filename = os.path.join(output_folder, '{}_{}.csv.gz'.format(prefix, filename))
    with gzip.open(filename, 'r') as f:
        return np.loadtxt(f, delimiter=', ', dtype=float)

def read_output_folder(output_folder):
    dfs = []
    for filename in glob.glob(os.path.join(output_folder, 'params*json')):
        filename = os.path.split(filename)[-1]
        filename = filename.replace('params_', '').replace('.json', '')
        params = read_json(output_folder, filename)
        π = read_csv_gz(output_folder, filename, 'π')
        ϵ = read_csv_gz(output_folder, filename, 'ϵ')
        η = read_csv_gz(output_folder, filename, 'η')
        μ = read_csv_gz(output_folder, filename, 'μ')
        t = np.arange(len(π))
        ϵ = ϵ[:len(t)]
        dfs.append(pd.DataFrame(dict(ID=filename, t=t, π=π, ϵ=ϵ, η=η, μ=μ, **params)))
    return pd.concat(dfs)

def load_simulations(folder, load_η, load_μ):
    dfs = []
    for filename in glob.glob(os.path.join(folder, 'params*json')):
        filename = os.path.split(filename)[-1]
        filename = filename.replace('params_', '').replace('.json', '')
        try:
            params = read_json(folder, filename)
            π = read_csv_gz(folder, filename, 'π')
            ϵ = read_csv_gz(folder, filename, 'ϵ')
            if load_η:
                η = read_csv_gz(folder, filename, 'η')
            if load_μ:
                μ = read_csv_gz(folder, filename, 'μ')
        except IOError:
            print("Faled loading", filename)
            continue
        t = np.arange(len(π))
        ϵ = ϵ[:len(t)]
        data = dict(ID=filename, t=t, π=π, ϵ=ϵ, **params)
        if load_η:
            data['η'] = η
        if load_μ:
            data['μ'] = μ
        dfs.append(pd.DataFrame(data))
    return pd.concat(dfs)

def deterministic(N, n, η, μ, ωA, ωB, π0, ϵ=None):
    if μ > 0:
        raise NotImplementedError("μ not implemented")
    π = [None] * n # π values
    f = [None] * n # frequency of π values
    if isinstance(π0, (float, int)):
        π[0] = [π0]
        f[0] = [1]
    else:
        π[0], f[0] = π0()

    for t in range(1, n):
        ωA_ = ωA * (ϵ[t]==0) + ωB * (ϵ[t]==1) # fitness of A at time t
        ωB_ = ωA * (ϵ[t]==1) + ωB * (ϵ[t]==0) # fitness of B at time t

        # all possible π values at time t+1
        π_ = [x * (1 - η) + η for x in π[t-1]] + [x * (1 - η) for x in π[t-1]]
        # frequencies for π_
        f_ = [
            f[t-1][i] * x * ωA_
            for i, x in enumerate(π[t-1])
        ] + [
            f[t-1][i] * (1 - x) * ωB_
            for i, x in enumerate(π[t-1])
        ]
        # remove π values for which f<1/N
        fsum = np.sum(f_)
        π[t] = [x for x, fx in zip(π_, f_) if (fx/fsum) > (1/N)]
        f_ = [fx for fx in f_ if (fx/fsum) > (1/N)]
        # normalize frequencies
        fsum = np.sum(f_)
        f[t] = [fx/fsum for fx in f_]

        assert len(f[t]) == len(π[t])
        assert all((0 <= fx <= 1 for fx in f[t]))
        assert all((0 <= x <= 1 for x in π[t]))
    return π, f


def uniform(n):
    return [1/(n-1) * x for x in range(n)], [1/n for x in range(n)]

def parse_env(env, n):
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
    elif env == 'ABAB':
        ϵ = np.array([0, 1] * (n // 2))
    else:
        m = env_pattern.match(env)
        if not m:
            raise ValueError("Unknown value for env: {}".format(env))
        k = int(m.groupdict()['k'])
        l = int(m.groupdict()['l'])
        ϵ = np.array(([0] * k + [1] * l) * (n // (k+l) + 1))[:n]
    return ϵ

def parse_π0(π0):
    π0 = str(π0)
    try:
        if π0 == 'U':
            π0 = lambda N: np.random.uniform(0, 1, N)
        elif π0[0] == 'N':
            π0_ = float(π0[1:])
            π0 = lambda N: np.random.normal(π0_, np.sqrt(π0_ / 10), N)
        elif π0[0] == 'C':
            π0_ = float(π0[1:])
            π0 = lambda N: np.ones(N) * π0_
        else:
            # if π0 is a float, using Normal(π0, π0/10)
            π0_ = float(π0)
            π0 = lambda N: np.random.normal(π0_, np.sqrt(π0_ / 10), N)
    except ValueError:
        raise ValueError("Unknown value for π0: {}".format(π0))
    return π0

def _main(N, n, η1, η2, μ1, μ2, ω0, ω1, π0, κ, env, output_folder):
    params = dict(N=N, n=n, η1=η1, η2=η2, μ1=μ1, μ2=μ2, ω0=ω0, ω1=ω1, π0=π0, κ=κ, env=env)
    now = datetime.datetime.now()
    click.echo("Simulation started: {}".format(now, params))

    ϵ = parse_env(env, n)
    π0 = parse_π0(π0)

    if η2 is None and μ2 is None:
        π = simulation(N, n, η1, μ1, ω0, ω1, π0, ϵ)
    else:
        if μ2 is None:
            μ2 = μ1
        if η2 is None:
            η2 = η1
        π, η_bar, μ_bar = simulation_modifiers(N, n, η1, η2, μ1, μ2, ω0, ω1, π0, κ, ϵ)

    filename = now.isoformat().replace(':', '-')
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    write_json(output_folder, filename, params)
    write_csv_gz(output_folder, filename, 'π', π.mean(axis=1))
    write_csv_gz(output_folder, filename, 'ϵ', ϵ)    
    if η2 is not None and η2 != η1:
        write_csv_gz(output_folder, filename, 'η', η_bar)
    if μ2 is not None and μ2 != μ1:
        write_csv_gz(output_folder, filename, 'μ', μ_bar)


@click.command()
@click.version_option(version=__version__, prog_name=__name__)
@click.option('--Ne', default=1000, help="Population size")
@click.option('--n', default=10, help="Number of generations")
@click.option('--η1', default=0.0, help="Learning rate")
@click.option('--η2', default=None, help="Invader modifier learning rate")
@click.option('--μ1', default=0.0, help="Mutation rate")
@click.option('--μ2', default=None, type=float, help="Invader modifier mutation rate")
@click.option('--ω0', default=2.0, help="Fitness of phenotype 0 in environment 0")
@click.option('--ω1', default=0.0, help="Fitness of phenotype 0 in environment 1")
@click.option('--π0', default='0.5', type=str, help="Initial density of phenotype 0; one of Nx, U, Cx, x where 0<x<1, N is normal (default), U is uniform, C is constant.")
@click.option('--κ', default=0.0, help="Modifier mutation rate")
@click.option('--env', default='A', type=str, 
    help="Type of environment: A, B, C correspond to Fig. 2; AkBl is a deterministic periodic environment with k As followed by l Bs")
@click.option('--output_folder', default='output', type=click.Path(), help="Output folder to which results will be written, defaults to 'output'")
@click.option('--reps', default=1, type=click.IntRange(1, None, clamp=False), help="Number of simulations to run")
@click.option('--cpus', default=1, help="Number of CPUs to use; if non-positive, will use all available CPUs")
def main(ne, n, η1, η2, μ1, μ2, ω0, ω1, π0, κ, env, output_folder, reps=1, cpus=1):
    repeat(_main, reps, cpus, N=ne, n=n, η1=η1, η2=η2, μ1=μ1, μ2=μ2, ω0=ω0, ω1=ω1, π0=π0, κ=κ, env=env, output_folder=output_folder)


if __name__ == '__main__':
    main()
