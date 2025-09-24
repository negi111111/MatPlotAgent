import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Prepare data
x = np.arange(1, 21)  # x-values from 1 to 20
y = np.random.uniform(low=-10, high=10, size=20)  # 20 random y-values between -10 and 10

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Uniform transparency
colors1 = ['blue' if val > 0 else 'orange' for val in y]
bars1 = ax1.bar(x, y, color=colors1, alpha=0.5, edgecolor=colors1, linewidth=1.5)
ax1.set_title("Uniform transparency value for all bars and edges")
ax1.set_xlabel("X Values")
ax1.set_ylabel("Y Values")

# Second subplot: Adjusted transparency
abs_y = np.abs(y)
normalized_abs_y = (abs_y - abs_y.min()) / (abs_y.max() - abs_y.min() + 1e-10)  # Normalize absolute y-values
for i in range(len(x)):
    face_alpha = normalized_abs_y[i]
    color = 'blue' if y[i] > 0 else 'orange'
    bar = ax2.bar(x[i], y[i], color=color, alpha=face_alpha, linewidth=1.5)
    bar[0].set_edgecolor(color)  # Edge color matches face color

ax2.set_title("Adjusted transparencies for each bar and each edge")
ax2.set_xlabel("X Values")
ax2.set_ylabel("Y Values")

# Adjust layout
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig("novice.png")