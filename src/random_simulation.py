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
from simulation import _main as simulation_main

@click.command()
@click.version_option(version=__version__, prog_name=prog_name)
@click.option('--Ne', default=None, type=int, help="Population size")
@click.option('--n', default=500, help="Number of generations")
@click.option('--η', default=None, type=float, help="Learning rate")
@click.option('--ω0', default=1.0, help="Fitness of phenotype 0 in environment 0")
@click.option('--ω1', default=None, type=float, help="Fitness of phenotype 0 in environment 1")
@click.option('--π0', default='0.5', type=str, help="Initial density of phenotype 0; one of Nx, U, Cx, x where 0<x<1, N is normal (default), U is uniform, C is constant.")
@click.option('--env', default='A', type=str, 
    help="Type of environment: A, B, C correspond to Fig. 2; AkBl is a deterministic periodic environment with k As followed by l Bs")
@click.option('--output_folder', default='output', type=click.Path(), help="Output folder to which results will be written, defaults to 'output'")
@click.option('--reps', default=1, type=click.IntRange(1, None, clamp=False), help="Number of simulations to run")
@click.option('--cpus', default=1, help="Number of CPUs to use; if non-positive, will use all available CPUs")
def main(ne, n, η, ω0, ω1, π0, env, output_folder, reps=1, cpus=1):
	repeat(_main, reps, cpus, N=ne, n=n, η=η, ω0=ω0, ω1=ω1, π0=π0, env=env, output_folder=output_folder)

def _main(N, n, η, ω0, ω1, π0, env, output_folder):
	if N is None:
		N = 10**np.random.randint(3, 7)
	if η is None:
		η = 10**np.random.uniform(-3, -1)
	if ω1 is None:
		ω1 = 10**np.random.uniform(-2, -1)
	simulation_main(N, n, η, None, 0, None, ω0, ω1, π0, 0, env, output_folder)


if __name__ == '__main__':
	main()