# Xue2016
Reproducing results of Xue &amp; Leiber, PNAS 2016

## Setting up

Download and install [Anaconda](https://www.continuum.io/downloads) or [Miniconda](http://conda.pydata.org/miniconda.html) to get Python and the conda package manager.

Then run these commands to update conda, create a virtual environment and install required packages:

```sh
conda update conda pip -y
conda config --add channels conda-forge
conda env create -f environment.yml
```

Remove `source` if running on Windows.

## Running a simulation

Activate the virtual environment:

```sh
source activate Xue2016
```

and start the simulation:

TBD