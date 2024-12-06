import random
from itertools import permutations

# ... existing random number generation code ...

# Example of permutations
def print_permutations(items):
    # Generate all permutations
    perms = list(permutations(items))
    print(f"\nAll permutations of {items}:")
    for i, perm in enumerate(perms, 1):
        print(f"Permutation {i}: {perm}")

# Example usage
sample_list = [1, 2, 3]
print_permutations(sample_list)