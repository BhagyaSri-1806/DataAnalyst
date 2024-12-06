# Independent variables
time = [0, 1, 2, 3, 4, 5]  # Time in hours
speed = 60  # Speed in miles per hour

# Calculate dependent variable (distance)
distance = []  # Distance is dependent on time and speed
for t in time:
    d = speed * t  # Distance = Speed × Time
    distance.append(d)

# Print results
print("Time (hours) | Distance (miles)")
print("-" * 30)
for t, d in zip(time, distance):
    print(f"{t:11} | {d:15}")

# Optional: Plot the relationship using matplotlib
import matplotlib.pyplot as plt

plt.plot(time, distance, 'b-o')
plt.title('Distance vs Time')
plt.xlabel('Time (hours)')
plt.ylabel('Distance (miles)')
plt.grid(True)
plt.show()