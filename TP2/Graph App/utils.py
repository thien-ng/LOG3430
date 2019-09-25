import random as rand

def bernoulli(p):
    '''
    Returns a random boolean from a Bernoulli distribution with success probability p.
    @param  p the probability of returning true
    @return true with probability p and false with probability 1 - p
    @raises ValueError unless 0 <= p <= 1.0
    '''
    if p < 0.0 or p > 1.0:
        raise ValueError("probability p must be between 0.0 and 1.0: " + p)
    return rand.uniform(0.0, p)