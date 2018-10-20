data {
    int n_samples; // number of times population sampled
    int sample_sizes[n_samples]; // available sample size per sample event
    int n; // total number of captures
    int freq[n]; // recapture frequency
    int min_bound; // number of unique labels -> minimum population size
}

parameters {
    real<lower=1> lambda_ss; // simple lower bound to sample size rate
    real<lower=min_bound> pop; // estimated population
}

transformed parameters {
    real lambda_pop;                            // back-of-the-envelope formula
    lambda_pop = (lambda_ss * n_samples) / pop; // for centering distribution
}                                               // given sampling conditions

model {
    sample_sizes ~ poisson(lambda_ss); // sample event rate
    for (i in 1:n) {
        freq[i] ~ poisson(lambda_pop)T[1, ]; // labels counted 0 times
    }                                        // unobservable -> all freq
}                                            // part of truncated distribution
