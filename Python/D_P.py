import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from collections import defaultdict

def collatz_sequence(n):
    """Generate the Collatz sequence for a given number n."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def collatz_tree(limit=100):
    """Construct a graph representation of the Collatz sequences up to a limit."""
    G = nx.DiGraph()
    for i in range(1, limit + 1):
        seq = collatz_sequence(i)
        for j in range(len(seq) - 1):
            G.add_edge(seq[j], seq[j + 1])
    return G

def plot_collatz_tree(G):
    """Visualize the Collatz tree using NetworkX."""
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=300, font_size=8, alpha=0.7)
    plt.title("Collatz Tree Representation")
    plt.show()

def transition_probabilities(N=10000):
    """Estimate transition probabilities of even/odd numbers."""
    even_to_even, even_to_odd, odd_to_even = 0, 0, 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            if (i // 2) % 2 == 0:
                even_to_even += 1
            else:
                even_to_odd += 1
        else:
            odd_to_even += 1  # 3n + 1 always results in even
            
    return {
        "P(even → even)": even_to_even / (even_to_even + even_to_odd),
        "P(even → odd)": even_to_odd / (even_to_even + even_to_odd),
        "P(odd → even)": 1.0  # Always transitions
    }

def expected_convergence_time(n):
    """Estimate the expected number of steps to reach 1."""
    steps = []
    for _ in range(1000):  # Run multiple simulations
        steps.append(len(collatz_sequence(n)))
    return np.mean(steps)

def plot_convergence_times(N=100):
    """Plot convergence times for numbers up to N."""
    times = [len(collatz_sequence(i)) for i in range(1, N + 1)]
    plt.figure(figsize=(10, 5))
    plt.bar(range(1, N + 1), times, color='blue', alpha=0.6)
    plt.xlabel("Starting Number")
    plt.ylabel("Steps to Reach 1")
    plt.title("Collatz Convergence Times")
    plt.show()

# Run analysis
G = collatz_tree(1000)
plot_collatz_tree(G)

trans_probs = transition_probabilities(1_000_000)
print("Transition Probabilities:", trans_probs)

plot_convergence_times(100)
