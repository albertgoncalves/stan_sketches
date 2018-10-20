#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# via http://isaacslavitt.com/2015/12/19/german-tank-problem-with-pymc-and-pystan/

from numpy.random import randint

from stanfuns import build_model


def obs_tanks(pop, n_obs):
    return randint(0, pop, n_obs)


def main():
    pop       = 1000
    n_obs     = 10
    obs       = obs_tanks(pop, n_obs)
    data      = {'n_obs': n_obs, 'obs': obs}
    stan_file = 'german_tanks.stan'
    model     = build_model(stan_file)
    fit       = model.sampling(data=data, n_jobs=-1)

    print(fit)


if __name__ == '__main__':
    main()
