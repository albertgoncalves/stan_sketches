data {
    int n_samples;
    int sample_sizes[n_samples];
    int n;
    int freq[n];
    int min_bound;
}

parameters {
    real<lower=1>         k;
    real<lower=min_bound> pop;
}

transformed parameters {
    real x;
    x = (k * n_samples) / pop;
}

model {
    sample_sizes ~ poisson(k);
    for (i in 1:n) {
        freq[i] ~ poisson(x)T[1, ];
    }
}
