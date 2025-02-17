import math

def binomial_call(S0, K, T, r, sigma, steps=100):
    """
    Binomial tree pricing (Cox-Ross-Rubinstein) for a European call.
    """
    if T <= 0:
        return max(S0 - K, 0.0)

    dt = T / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    q = (math.exp(r * dt) - d) / (u - d)

    # Terminal prices
    ST = [S0 * (u**j) * (d**(steps - j)) for j in range(steps + 1)]
    values = [max(s - K, 0) for s in ST]

    # Work backward
    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            values[j] = math.exp(-r * dt) * (q * values[j + 1] + (1 - q) * values[j])

    return values[0]
 
