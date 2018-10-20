#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# via https://youtu.be/MTmnVBJ9gCI?t=176

from collections import Counter
from functools   import reduce

import matplotlib.pyplot as plt
import numpy as np


def sample_counts(subpop, n_samples):
    return np.random.poisson(subpop, n_samples)


def label_samples(pop):
    return lambda count: np.random.randint(0, pop, count).tolist()


def flatten(list_of_lists):
    return reduce(lambda a, b: a + b, list_of_lists)


def generate_data(subpop, n_samples):

    def sample_pop(pop):
        sample_sizes = sample_counts(subpop, n_samples)
        labels       = flatten(map(label_samples(pop), sample_sizes))
        count_labels = Counter(labels)
        distribution = Counter(list(count_labels.values()))
        return distribution

    return sample_pop


def sort_dict(dct):
    return {key: dct[key] for key in sorted(dct.keys())}


def main():

    def plot_dict(dct, label, ax, kwargs):
        ax.bar(list(dct.keys()), list(dct.values()), **kwargs)
        ax.set_title(label)

    conditions = generate_data(subpop=20, n_samples=20)
    pop_sizes  = [50, 100, 200, 500]
    kwargs     = {'width': 1, 'color': '0.15'}

    fig, axs = plt.subplots(len(pop_sizes), 1, sharex=True, figsize=(9, 6))

    for i, pop_size in enumerate(pop_sizes):
        dct = sort_dict(conditions(pop=pop_size))
        plot_dict(dct, pop_size, axs[i], kwargs)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
