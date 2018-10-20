#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import listdir
from pickle import dump
from pickle import load

from pystan import StanModel


def build_model(stan_file):
    pkl_file = stan_file.replace('.stan', '.pkl')

    if pkl_file not in listdir():
        model = StanModel(file=stan_file)
        pickle_to_file(model, pkl_file)
    else:
        model = pickle_from_file(pkl_file)

    return model


def pickle_from_file(file_path):
    with open(file_path, 'rb') as f:
        pickle_content = load(f)

    return pickle_content


def pickle_to_file(pickle_content, file_path):
    with open(file_path, 'wb') as f:
        dump(pickle_content, f)
