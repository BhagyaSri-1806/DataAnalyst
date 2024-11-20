import random
from collections import Counter

class DiscreteRandomVariable:
    def __init__(self, outcomes):
        self.outcomes = outcomes
        self.probability_distribution = self.calculate_probability_distribution()

    def calculate_probability_distribution(self):
        """Calculate the probability distribution of the outcomes."""
        total_outcomes = len(self.outcomes)
        outcome_counts = Counter(self.outcomes)
        probabilities = {outcome: count / total_outcomes for outcome, count in outcome_counts.items()}
        return probabilities

    def probability_mass_function(self, value):
        """Return the probability of a specific outcome."""
        return self.probability_distribution.get(value, 0)

# Simulate rolling a die 1000 times
num_rolls = 1000
outcomes = [random.randint(1, 6) for _ in range(num_rolls)]

# Create a discrete random variable for the die rolls
die_rolls = DiscreteRandomVariable(outcomes)

# Display the probability mass function
print("Probability Mass Function (PMF) for die rolls:")
for outcome in range(1, 7):
    probability = die_rolls.probability_mass_function(outcome)
    print(f"Outcome {outcome}: {probability:.2f}")