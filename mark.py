#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# via https://en.wikipedia.org/wiki/Mark_and_recapture#More_than_two_visits

from collections   import Counter

from mark_research import flatten
from mark_research import label_samples
from mark_research import sample_counts
from stanfuns      import build_model


def label_captures(pop, sample_sizes):
    return flatten(map(label_samples(pop), sample_sizes))


def main():
    pop          = 750  # population to be estimated from generated data
    subpop       = 20   # "true" sample event rate
    n_samples    = 10   # number of capture events
    sample_sizes = sample_counts(subpop, n_samples)   # sample event sizes
    labels       = label_captures(pop, sample_sizes)  # sampled pop labels
    label_counts = Counter(labels)  # {label: recapture frequency}
    freq         = list(label_counts.values())  # don't need labels, just freq!
    min_bound    = len(label_counts.keys())  # number of unique labels
    data         = { 'n_samples'   : n_samples
                   , 'sample_sizes': sample_sizes
                   , 'n'           : len(freq)
                   , 'freq'        : freq
                   , 'min_bound'   : min_bound
                   }
    stan_file    = 'mark.stan'
    model        = build_model(stan_file)
    fit          = model.sampling(data=data, n_jobs=-1, refresh=-1)

    print(fit.stansummary(['pop', 'lambda_ss']))


if __name__ == '__main__':
    main()
