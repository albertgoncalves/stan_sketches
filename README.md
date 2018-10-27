# Stan Sketches

A small collection of toy statistical models using [Stan](http://mc-stan.org/) via Python.

Needed things
---
  * Python 3.x
  * NumPy
  * PyStan
  * Matplotlib
---
If you have [Conda](https://anaconda.org/) you can get rolling without too much trouble:
```bash
$ conda create -n MYENV python=3 numpy pystan matplotlib
$ conda activate MYENV
(MYENV) $ python FILENAME.py
```
---
In order to reduce compilation time, each model script will [pickle](https://docs.python.org/3/library/pickle.html) the compiled `StanModel` to `./FILENAME.pkl`. If you wish to re-compile any given model, simply delete the respective `.pkl` file prior to running the model's Python script.
