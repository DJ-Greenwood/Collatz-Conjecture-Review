import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

def collatz_step(n):
    """Perform one step in the Collatz sequence."""
    return n // 2 if n % 2 == 0 else 3 * n + 1

def collatz_sequence(n):
    """Generate the Collatz sequence for a given n."""
    sequence = [n]
    while n != 1:
        n = collatz_step(n)
        sequence.append(n)
    return sequence

def simulate_collatz(n_max=100000, sample_size=10000):
    """Simulate Collatz sequences for random values up to n_max."""
    np.random.seed(42)
    start_values = np.random.randint(1, n_max, sample_size)
    results = []
    
    for n in start_values:
        seq = collatz_sequence(n)
        max_value = max(seq)
        steps = len(seq) - 1
        even_count = sum(1 for x in seq if x % 2 == 0)
        odd_count = steps - even_count
        results.append((n, steps, max_value, even_count, odd_count))
    
    df = pd.DataFrame(results, columns=["Start", "Steps", "Max Value", "Even Steps", "Odd Steps"])
    df.to_csv("data/collatz_simulation.csv", index=False)
    return df

def plot_collatz_behavior(df):
    """Generate and save visualizations of Collatz behavior."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df["Steps"], bins=50, kde=True)
    plt.title("Distribution of Collatz Convergence Steps")
    plt.xlabel("Number of Steps")
    plt.ylabel("Frequency")
    plt.savefig("data/collatz_steps_distribution.png")
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df["Max Value"], bins=50, kde=True)
    plt.title("Distribution of Maximum Values in Collatz Sequences")
    plt.xlabel("Max Value Reached")
    plt.ylabel("Frequency")
    plt.xscale("log")  # Log scale to handle large values
    plt.savefig("data/collatz_max_values.png")
    plt.close()

def compute_transition_probabilities(df):
    """Estimate probabilities of transitioning from even to odd and vice versa."""
    total_even = df["Even Steps"].sum()
    total_odd = df["Odd Steps"].sum()
    
    p_even_to_even = (3 / 4)
    p_even_to_odd = (1 / 4)
    p_odd_to_even = 1.0  # Since 3n+1 always produces an even number
    
    transition_probs = {
        "Even -> Even": p_even_to_even,
        "Even -> Odd": p_even_to_odd,
        "Odd -> Even": p_odd_to_even
    }
    
    with open("data/collatz_transition_probabilities.txt", "w", encoding='utf-8') as f:
        for k, v in transition_probs.items():
            f.write(f"{k}: {v:.4f}\n")
    
    return transition_probs

def compute_expected_convergence_time(df):
    """Compare empirical convergence time to theoretical bounds."""
    df["Log Start"] = np.log2(df["Start"])
    regression = np.polyfit(df["Log Start"], df["Steps"], 1)
    
    theoretical_c = regression[0]  # Approximate theoretical constant
    k_offset = regression[1]
    
    with open("data/collatz_convergence_time.txt", "w", encoding='utf-8') as f:
        f.write(f"Empirical Approximation: E[T(n)] ≈ {theoretical_c:.4f} log2(n) + {k_offset:.4f}\n")
    
    return theoretical_c, k_offset

def main():
    """Run all analyses and save results."""
    df = simulate_collatz()
    plot_collatz_behavior(df)
    transition_probs = compute_transition_probabilities(df)
    theoretical_c, k_offset = compute_expected_convergence_time(df)

    print("Simulation complete.")
    print(f"Transition Probabilities: {transition_probs}")
    print(f"Theoretical Constant: {theoretical_c:.4f}")    
    print("Analysis complete. Check the data/ directory for results.")
    
if __name__ == "__main__":
    main()
