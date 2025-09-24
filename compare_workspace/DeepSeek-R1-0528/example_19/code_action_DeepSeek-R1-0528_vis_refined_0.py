import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Define sales data in hundreds
sales_data = [
    [120, 95, 130, 85, 100],  # Apples
    [90, 115, 80, 105, 95],   # Oranges
    [75, 80, 85, 70, 90],     # Bananas
    [65, 70, 60, 75, 80],     # Grapes
    [55, 60, 65, 50, 55]      # Berries
]

regions = ['North', 'South', 'East', 'West', 'Central']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']  # Soft pastel colors
fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']

# Convert to numpy array for vector operations
sales_array = np.array(sales_data)
cumulative = np.zeros(len(regions))

# Create figure with constrained layout
fig, ax = plt.subplots(figsize=(10, 7), layout='constrained')

# Plot stacked bars
for i in range(len(sales_array)):
    ax.bar(regions, sales_array[i], bottom=cumulative, 
           color=colors[i], label=fruits[i], edgecolor='white', linewidth=0.5)
    cumulative += sales_array[i]

# Add total labels at top of bars
for i, total in enumerate(cumulative):
    ax.text(i, total + 5, f'{int(total)}', 
            ha='center', va='bottom', fontsize=9, fontweight='bold')

# Configure axes and title
ax.set_ylabel('Sales (in hundreds)', fontsize=10)
ax.set_title('Sales by Region', fontsize=12, fontweight='bold')
ax.set_xticks([])  # Remove x-axis labels
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Create data table (values in original units)
table_data = [[f'{val}' for val in row] for row in sales_data]
table = plt.table(cellText=table_data, 
                 colLabels=regions, 
                 rowLabels=fruits,
                 cellLoc='center', 
                 loc='bottom', 
                 bbox=[0, -0.45, 1, 0.3])

# Style table
table.auto_set_font_size(False)
table.set_fontsize(9)
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(fontweight='bold', color='white')
        cell.set_facecolor('#555555')
    elif col == -1:  # Row headers
        cell.set_text_props(fontweight='bold')
        cell.set_facecolor('#f0f0f0')

# Adjust layout and save
plt.savefig("novice_final.png", dpi=120, bbox_inches='tight')