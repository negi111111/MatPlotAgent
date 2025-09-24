import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Data and labels
sales_data = [
    [120, 95, 130, 85, 100],  # Apples
    [90, 115, 80, 105, 95],   # Oranges
    [75, 80, 85, 70, 90],     # Bananas
    [65, 70, 60, 75, 80],     # Grapes
    [55, 60, 65, 50, 55]      # Berries
]
fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']
regions = ['North', 'South', 'East', 'West', 'Central']
colors = ['#FFD1DC', '#FFB347', '#B0E57C', '#AEC6CF', '#D8BFD8']  # Soft pastel colors

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot stacked bars
x = np.arange(len(regions))
bottom = np.zeros(len(regions))

for i in range(len(fruits)):
    ax.bar(
        x, 
        sales_data[i], 
        bottom=bottom, 
        color=colors[i], 
        edgecolor='grey',
        linewidth=0.7
    )
    bottom += np.array(sales_data[i])

# Add total sales labels
total_sales = bottom
for i, total in enumerate(total_sales):
    ax.text(
        x=i, 
        y=total + 8, 
        s=f'{total:.0f}', 
        ha='center', 
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )

# Configure chart
ax.set_title('Sales by Region', fontsize=14, pad=20)
ax.set_ylabel('Sales (in hundreds)', fontsize=12)
ax.set_xticks([])
ax.set_ylim(0, max(total_sales) * 1.15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Format table data
table_data = []
for row in sales_data:
    formatted_row = [f'{(val / 100):.2f}' for val in row]
    table_data.append(formatted_row)

# Create table
table = ax.table(
    cellText=table_data,
    rowLabels=fruits,
    rowColours=colors,
    colLabels=regions,
    cellLoc='center',
    loc='bottom',
    bbox=[0, -0.5, 1, 0.3]
)

# Style table
table.auto_set_font_size(False)
table.set_fontsize(9)
for (row, col), cell in table.get_celld().items():
    if row == 0:  # Header row
        cell.set_text_props(weight='bold')
    cell.set_linewidth(0.5)

# Adjust layout and save
plt.subplots_adjust(bottom=0.25)
plt.savefig("novice.png", dpi=120, bbox_inches='tight')