import random

def flip_five_coins(num_trials=1000):
    # Dictionary to store count of heads
    results = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    
    for _ in range(num_trials):
        # Flip 5 coins (1 for heads, 0 for tails)
        flip_result = sum(random.choice([0, 1]) for _ in range(5))
        results[flip_result] += 1
    
    # Calculate and display probabilities
    print("\nProbabilities for getting heads:")
    for heads in range(6):
        probability = results[heads] / num_trials
        percentage = probability * 100
        print(f"{heads} heads: {percentage:.1f}%")

# Run the simulation
print("Simulating 1000 trials of flipping 5 coins...")
flip_five_coins()