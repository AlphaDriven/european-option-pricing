from option_pricing.black_scholes import black_scholes_call
from option_pricing.monte_carlo import monte_carlo_call
from option_pricing.binomial import binomial_call



def main():
    S0 = 100.0
    K = 105.0
    T = 1.0
    r = 0.05
    sigma = 0.20

    bs_price = black_scholes_call(S0, K, T, r, sigma)
    print(f"Black-Scholes Call Price: {bs_price:.4f}")

    mc_price = monte_carlo_call(S0, K, T, r, sigma, num_simulations=100000, seed=42)
    print(f"Monte Carlo Call Price:   {mc_price:.4f}")

    bin_price = binomial_call(S0, K, T, r, sigma, steps=100)
    print(f"Binomial Tree Call Price: {bin_price:.4f}")

if __name__ == "__main__":
    main()
 
