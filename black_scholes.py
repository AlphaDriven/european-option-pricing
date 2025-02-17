import math
from math import log, sqrt, exp
from scipy.stats import norm

def black_scholes_call(S0, K, T, r, sigma):
    """
    Black-Scholes formula for a European call.
    """
    if T <= 0:
        return max(S0 - K, 0.0)

    d1 = (log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    return S0 * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)

