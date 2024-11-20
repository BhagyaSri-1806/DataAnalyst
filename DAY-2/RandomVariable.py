import random
from collections import Counter

def roll_die(num_rolls):
    """Simulate rolling a six-sided die num_rolls times."""
    outcomes = [random.randint(1, 6) for _ in range(num_rolls)]
    return outcomes

def calculate_probabilities(outcomes):
    """Calculate the probability of each outcome."""
    total_rolls = len(outcomes)
    outcome_counts = Counter(outcomes)
    probabilities = {outcome: count / total_rolls for outcome, count in outcome_counts.items()}
    return probabilities

# Simulate rolling a die 1000 times
num_rolls = 1000
outcomes = roll_die(num_rolls)

# Calculate probabilities
probabilities = calculate_probabilities(outcomes)

# Display results
print("Outcome probabilities after rolling a die 1000 times:")
for outcome, probability in sorted(probabilities.items()):
    print(f"Outcome {outcome}: {probability:.2f}")