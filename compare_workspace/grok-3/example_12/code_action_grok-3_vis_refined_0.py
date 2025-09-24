import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Set a fixed seed for reproducibility
np.random.seed(42)

# Generate X and Y values
x_values = np.arange(1, 21)
y_values = np.random.randint(-10, 10, size=20)  # Random y values between -10 and 10

# Determine bar colors (blue for y > 0, orange for y <= 0)
colors = ['blue' if y > 0 else 'orange' for y in y_values]

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# First bar chart with uniform transparency
ax1.bar(x_values, y_values, color=colors, alpha=0.5, edgecolor='black', linewidth=1)
ax1.set_title("Uniform transparency value for all bars and edges")
ax1.set_xlabel("X Values")
ax1.set_ylabel("Y Values")

# Normalize Y values for the second bar chart
abs_y_values = np.abs(y_values)
max_abs_y = np.max(abs_y_values)
face_alphas = abs_y_values / max_abs_y  # Normalize to get face alpha values
edge_alphas = 1 - face_alphas  # Ensure sum of face and edge alpha is 1

# Second bar chart with adjusted transparencies
for i in range(len(x_values)):
    ax2.bar(x_values[i], y_values[i], color=colors[i], alpha=face_alphas[i], 
            edgecolor=colors[i], linewidth=1)  # Note: Matplotlib doesn't support separate edge alpha directly

ax2.set_title("Adjusted transparencies for each bar and edge")
ax2.set_xlabel("X Values")
ax2.set_ylabel("Y Values")

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("novice_final.png")