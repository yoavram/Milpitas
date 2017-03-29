# -*- coding: utf-8 -*-
"""
TODO

Created on Thu Nov 17 16:24:45 2016

@author: yoav@yoavram.com
"""
import click
from ultrachronic import repeat
import numpy as np
from simulation import __version__
from simulation import __name__ as prog_name
from simulation import _main

def min_l_for_fixation(k, η, W, w):
    return k * (1 + (1 - η) *(W - w) / w)

def max_l_for_no_fixation(k, η, W, w):
    return k * (1 + ((1 - η) *(W - w) / w)/(1+η*(1 - η)*(W-w)**2/(W*w)))

@click.command()
@click.version_option(version=__version__, prog_name=prog_name)
@click.option('--Ne', default=None, type=int, help="Population size")
@click.option('--ω0', default=1.0, help="Fitness of phenotype 0 in environment 0")
@click.option('--π0', default='0.5', type=str,
              help="Initial density of phenotype 0; one of Nx, U, Cx, x where 0<x<1, N is normal (default), U is uniform, C is constant.")
@click.option('--output_folder', default='output', type=click.Path(),
              help="Output folder to which results will be written, defaults to 'output'")
def main(ne, ω0, π0, output_folder):
    W = ω0
    N = ne
    η = round(10 ** np.random.uniform(-3, -1), 4)
    w = round(10 ** np.random.uniform(-2, -1), 4)
    k = int(np.random.randint(1, 40))

    Ls = [
        k,
        np.floor(max_l_for_no_fixation(k, η, W, w)) // 2,
        np.floor(max_l_for_no_fixation(k, η, W, w)),
        np.ceil(min_l_for_fixation(k, η, W, w)),
        2 * np.ceil(min_l_for_fixation(k, η, W, w)),
    ]
    Ls = map(int, Ls)

    for l in Ls:
        n = min(5000, int(100 * (k + l)))
        env = 'A{:d}B{:d}'.format(k, l)
        print('env={}, n={}'.format(env, n))
        _main(N, n, η, None, 0, None, W, w, π0, 0, env, output_folder)


if __name__ == '__main__':
    main()
