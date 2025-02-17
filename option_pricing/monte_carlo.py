import numpy as np
import math

def monte_carlo_call(S0, K, T, r, sigma, num_simulations=100_000, seed=None):
    """
    Monte Carlo pricing for a European call.
    """
    if T <= 0:
        return max(S0 - K, 0.0)

    if seed is not None:
        np.random.seed(seed)

    Z = np.random.randn(num_simulations)  # standard normal draws
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * math.sqrt(T) * Z)
    payoffs = np.maximum(ST - K, 0)
    return math.exp(-r * T) * np.mean(payoffs)
 
