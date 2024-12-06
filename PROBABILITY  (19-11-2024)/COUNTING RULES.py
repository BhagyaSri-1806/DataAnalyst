import math

def permutations(n, r):
    """Calculate the number of permutations (nPr)."""
    return math.factorial(n) // math.factorial(n - r)

def combinations(n, r):
    """Calculate the number of combinations (nCr)."""
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Example usage
n = 5  # Total items
r = 3  # Items to choose

# Calculate permutations and combinations
num_permutations = permutations(n, r)
num_combinations = combinations(n, r)

print(f"Number of permutations (nPr) of {n} items taken {r} at a time: {num_permutations}")
print(f"Number of combinations (nCr) of {n} items taken {r} at a time: {num_combinations}")
