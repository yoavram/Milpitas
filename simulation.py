## Automatically generated with __main__ from simulation.ipynb

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set(style='ticks', context='paper', font_scale=1.3)

def simulation(N, n, η, ω0, ω1, π0, ϵ=None):
    """Run a single simulation.
    
    Parameters
    ----------
    N : int
        constant population size
    n : int
        number of generations
    η : float
        learning rate, 0 <= η <= 1
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
        π[t + 1, :] = (1 - η) * π[t, idx] + η * (φ[idx] == 0)
        
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


def simulation_modifiers(N, n, η1, η2, ω0, ω1, π0, ϵ=None):
    """Run a single simulation.
    
    Parameters
    ----------
    N : int
        constant population size
    n : int
        number of generations
    η1, η2 : float
        learning rate, 0 <= η <= 1
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
        π[t + 1, :] = (1 - η) * π[t, idx] + η * (φ[idx] == 0)
    
    return π, η_bar


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
