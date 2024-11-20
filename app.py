import random

# Generate and print 100 random numbers
for i in range(100):
    # Generate random number between 1 and 1000
    random_number = random.randint(1, 1000)
    print(f"Number {i+1}: {random_number}")