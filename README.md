# Vertical and Oblique Transmission under Fluctuating Selection
## Yoav Ram, Uri Liberman, and Marcus W. Feldman, PNAS 2018

This repository contains supporting material for

>   Ram, Liberman & Feldman (2018) _Vertical and Oblique Transmission under Fluctuating Selection_, Proc Natl Acad Sci USA. DOI: [10.1073/pnas.1719171115](https://doi.org/10.1073/pnas.1719171115)

The notebook file [`figures.ipynb`](https://github.com/yoavram/Milpitas/blob/master/notebooks/figures.ipynb) includes Python source code for reproduction of the manuscript figures.

## Run the notebook

You can interact with the notebooks on your own machine.

### Install dependencies

The easiest way to install the dependencies is to install [Anaconda](https://www.anaconda.com/download/).
You should use Python 3, preferably with version 3.5 or higher.
The notebook will probably not work on Python 2.

All required packages should then be available.
However, if you get an `ImportError` due to a package not being installed, the following command will install all requirements using conda:

```sh
conda install jupyter numpy scipy matplotlib pandas seaborn sympy numba 
```

You also need to install [rakott](https://github.com/yoavram/rakott) and [matplotlib_colorbar](https://github.com/ppinard/matplotlib-colorbar):
```sh
pip install https://github.com/yoavram/rakott.git
pip install matplotlib_colorbar
```

### Get the source code repository

You can download all the source code by clicking the _Clone or Download_ button and choosing _Download ZIP_. Then extract the ZIP to a folder on your machine.

If you use `git` you can clone the repo using:

```sh
git clone https://github.com/yoavram/Milpitas.git
```

### Run the notebook

Start a Jupyter notebook server inside the repo folder:

```sh
cd <path to folder>
jupyter notebook
```

Your browser should open automatically. 
Open the `notebooks` folder and choose the notebook file `figures.ipynb` file.

## Troubleshooting

Use the [Issues](https://github.com/yoavram/Milpitas/issues) page to report problems or suggest improvements or contact [Yoav Ram](mailto:yoav@yoavram.com).

License
-------

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0
International License.
