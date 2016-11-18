# Xue2016
Reproducing results of Xue &amp; Leiber, PNAS 2016

## Setting up

Download and install [Anaconda](https://www.continuum.io/downloads) or [Miniconda](http://conda.pydata.org/miniconda.html) to get Python and the conda package manager.

Then run these commands to update conda, create a virtual environment and install required packages:

```sh
conda config --add channels conda-forge
conda update conda pip -y
conda env create -f environment.yml
```

Before using the notebook or the simulation you must always activate the environment you just created:

```sh
source activate Xue2016
```

Remove `source` if running on Windows.

## Using the notebook

The notebook allows you to reproduce the figure from Xue & Leibler 2016 and to run single simulations and plot their results.

To start the notebook, call `jupyter notebook` inside the repository folder.

## Running a simulation

To run a the simulation:

```sh
python simulation.py
```

To simulate a competition between two modifier alleles, specify `η2`.