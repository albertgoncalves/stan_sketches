data {
    int  n_obs;
    real obs[n_obs];
}

parameters {
    real<lower=max(obs)> pop;
}

model {
    obs ~ uniform(0, pop);
}
