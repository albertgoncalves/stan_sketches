data {
    int n_samples; // number of times population sampled
    int sample_sizes[n_samples]; // available sample size per sample event
    int n; // total number of captures
    int freq[n]; // recapture frequency
    int min_bound; // number of unique labels -> minimum population size
}

parameters {
    real<lower=1> sample_rate; // simple lower bound to sample size rate
    real<lower=min_bound> pop; // estimated population
}

transformed parameters {
    real lambda;                              // back-of-the-envelope formula
    lambda = (sample_rate * n_samples) / pop; // for centering distribution
}                                             // given sampling conditions

model {
    sample_sizes ~ poisson(sample_rate);
    for (i in 1:n) {
        freq[i]  ~ poisson(lambda)T[1, ]; // labels counted 0 times
    }                                     // unobservable -> all freq part of
}                                         // truncated distribution
