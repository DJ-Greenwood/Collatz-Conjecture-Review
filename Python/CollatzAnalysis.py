import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create necessary directories
DATA_DIR = "data"
IMAGE_DIR = os.path.join(DATA_DIR, "images")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

def collatz_steps(n):
    """Compute the number of steps to reach {16, 8, 4, 2, 1}."""
    steps = 0
    trajectory = []
    while n != 1 and n not in {16, 8, 4, 2}:  # Stop at the proven cycle
        trajectory.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    trajectory.append(n)
    return steps, trajectory

def categorize_number(n):
    """Categorize numbers into P (Powers of 2), O (Odd Numbers), and E (Even Numbers, Not Powers of 2)."""
    if n & (n - 1) == 0:
        return "P"  # Power of 2
    elif n % 2 == 1:
        return "O"  # Odd number
    else:
        return "E"  # Even number, not a power of 2

def analyze_collatz(range_limit=10000):
    """Analyze the Collatz conjecture for numbers up to range_limit."""
    results = []
    
    for n in range(1, range_limit + 1):
        steps, trajectory = collatz_steps(n)
        category = categorize_number(n)
        results.append((n, steps, category, trajectory))
    
    df = pd.DataFrame(results, columns=["Number", "Steps", "Category", "Trajectory"])
    df.to_csv(os.path.join(DATA_DIR, "collatz_results.csv"), index=False)
    return df

def plot_collatz_steps(df):
    """Generate and save a plot showing the number of steps per number."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Number"], df["Steps"], alpha=0.5, s=5)
    plt.xlabel("Starting Number")
    plt.ylabel("Steps to Reach {16, 8, 4, 2, 1}")
    plt.title("Collatz Steps Analysis")
    plt.savefig(os.path.join(IMAGE_DIR, "collatz_steps.png"))
    plt.show()

def plot_category_distribution(df):
    """
    Generate and save a bar chart showing the distribution of categories.
    Parameters:
    df (pandas.DataFrame): DataFrame containing the data with a 'Category' column.
    The function will create a bar chart with the counts of each category present in the 'Category' column
    of the DataFrame. The chart will be saved as 'category_distribution.png' in the directory specified by IMAGE_DIR.
    The categories are expected to be 'P', 'O', and 'E', and the bars will be colored blue, red, and green respectively.
    Returns:
    None
    """
    """Generate and save a bar chart showing the distribution of categories."""
    category_counts = df["Category"].value_counts()
    
    plt.figure(figsize=(8, 5))
    category_counts.plot(kind="bar", color=['blue', 'red', 'green'])
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.title("Distribution of Number Categories (P, O, E)")
    plt.xticks(rotation=0)
    plt.savefig(os.path.join(IMAGE_DIR, "category_distribution.png"))
    plt.show()

# Run analysis
df = analyze_collatz(1_000_000)
plot_collatz_steps(df)
plot_category_distribution(df)
