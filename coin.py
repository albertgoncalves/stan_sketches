#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# via http://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html

from random   import sample

from stanfuns import build_model


def post_draws(fit, key):
    return lambda f: sum(map(f, fit[key])) / len(fit[key])


def main():
    heads      = [1] * 10
    tails      = [0] * 4
    flips      = sample(heads + tails, 14)
    stan_file  = 'coin.stan'
    data       = { 'n'     : len(flips)
                 , 'flips' : flips
                 , 'post_n': 5
                 }
    model      = build_model(stan_file)
    fit        = model.sampling(data=data, n_jobs=-1, refresh=-1)

    post_flips = post_draws(fit, 'post_flips')
    outcomes   = [ ('H'    , lambda draw:  draw[0]  == 1)
                 , ('HH'   , lambda draw: (draw[:2] == 1).all())
                 , ('HHH'  , lambda draw: (draw[:3] == 1).all())
                 , ('HHHH' , lambda draw: (draw[:4] == 1).all())
                 , ('HHHHH', lambda draw: (draw     == 1).all())
                 ]

    print(fit.stansummary(['theta']), '\n')
    for label, f in outcomes:
        print( ('P({:' + str(len(outcomes)) + '}|theta: ').format(label)
             + '{0:.4f})'.format(post_flips(f))
             )


if __name__ == '__main__':
    main()
