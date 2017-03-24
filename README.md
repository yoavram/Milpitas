## Setting up

Download and install [Anaconda](https://www.continuum.io/downloads) or [Miniconda](http://conda.pydata.org/miniconda.html) to get Python **3.5** and the conda package manager.

Run these commands to update conda, create a virtual environment and install required packages:

```sh
conda config --add channels conda-forge
conda update conda pip -y
conda create env -n Milpitas -f environment.yml
```
## Using the notebooks

The notebooks allow you to reproduce the figures and to run single simulations and plot their results.

To start the notebooks, call `jupyter notebook` inside the repository folder, and then browse over to the `notebooks` folder.

## Running simulations

To get help for the simulation:

```sh
python src/simulation.py --help
```

to run them:

```sh
python src/simulation.py --Ne 100000 --n 500 --η1 0.1 --ω0 2.0 --ω1 0.2  --π0 0.5  --env A
```

To simulate a competition between two modifier alleles, specify `--η2 0.2` (with `η2>η1`).

To run simulations on SGE cluster, call

```sh
qsub -t 1-1000 -v env=C cluster/simulation.sge'
```

replacing `1000` with the required number of replicate simulations, and `C` with the environment name (`A`, `B` and `C`).

Output files (`params_?.json` and `x_?.csv.gz` files will be written to the `output` folder, where `?` is replaced by a date and time of the simulation and `x` by `π`, `ϵ` and `η` for the average `π` over time, the environments, and the average `η` over time (if `η2` was specified).

You can tar these files to an archive with `tar czf output.tgz output` and untar them with `tar xzf output.tgz`.
