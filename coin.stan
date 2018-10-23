data {
    int<lower=1> n;
    int<lower=0, upper=1> flips[n];
    int<lower=1> post_n;
}

parameters {
    real<lower=0, upper=1> theta;
}

model {
    theta ~ beta(1, 1);
    flips ~ bernoulli(theta);
}

generated quantities {
    int<lower=0, upper=1> post_flips[post_n];

    for (i in 1:post_n) {
        post_flips[i] = bernoulli_rng(theta);
    }
}
