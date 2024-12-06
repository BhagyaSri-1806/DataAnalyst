import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mean = 0
std_dev = 1

# Generate random samples from a normal distribution
num_samples = 1000
samples = np.random.normal(mean, std_dev, num_samples)

# Calculate the probability density function (PDF)
x = np.linspace(-4, 4, 1000)
pdf = norm.pdf(x, mean, std_dev)

# Plot the histogram of the samples and the PDF
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=30, density=True, alpha=0.6, color='b', label='Histogram of samples')
plt.plot(x, pdf, 'r', label='PDF of normal distribution')
plt.title('Normal Distribution (mean=0, std_dev=1)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()