import matplotlib
matplotlib.use('Agg')
"""
Deterministic script that creates a stacked-bar chart of fruit sales across
five regions, adds cumulative totals above each stack, appends a colour-coded
data table underneath, and saves the figure as `novice_final.png`.

Only NumPy and Matplotlib are used to comply with library restrictions.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# 1. Data ----------------------------------------------------------------
sales_data = [
    [120, 95, 130, 85, 100],  # Apples
    [90, 115, 80, 105, 95],   # Oranges
    [75, 80, 85, 70, 90],     # Bananas
    [65, 70, 60, 75, 80],     # Grapes
    [55, 60, 65, 50, 55]      # Berries
]
regions = ['North', 'South', 'East', 'West', 'Central']
fruits  = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']

sales_data = np.array(sales_data)

# ---------------------------------------------------------------------
# 2. Figure & axes ------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# Soft pastel colours for each fruit category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

bar_width     = 0.6
bottom_values = np.zeros(len(regions))

# ---------------------------------------------------------------------
# 3. Stacked bars -------------------------------------------------------
for idx, fruit in enumerate(fruits):
    ax.bar(
        regions,
        sales_data[idx],
        bar_width,
        bottom=bottom_values,
        color=colors[idx],
        edgecolor='white',
        label=fruit
    )
    bottom_values += sales_data[idx]

# ---------------------------------------------------------------------
# 4. Titles, labels, cumulative totals ---------------------------------
ax.set_title('Sales by Region')
ax.set_ylabel('Sales (Hundreds)')
ax.set_xlabel('')            # Explicitly leave x-axis label blank
ax.set_ylim(0, bottom_values.max() + 30)  # Add headroom for text

for i, total in enumerate(bottom_values):
    ax.text(
        i, total + 5,               # Slightly above the bar
        str(total),
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )

# ---------------------------------------------------------------------
# 5. Data table ---------------------------------------------------------
# Convert numbers to string values in hundreds (two decimals)
cell_text = [[f"{val/100:.2f}" for val in row] for row in sales_data]

# The table goes underneath the chart
table = plt.table(
    cellText=cell_text,
    colLabels=regions,
    rowLabels=fruits,
    rowColours=colors,             # Match row label background to bar colour
    cellLoc='center',
    loc='bottom',
    bbox=[0.05, -0.45, 0.9, 0.35]  # [left, bottom, width, height]
)

table.auto_set_font_size(False)
table.set_fontsize(8)

# ---------------------------------------------------------------------
# 6. Layout adjustments & save -----------------------------------------
plt.subplots_adjust(bottom=0.35)   # Make room for the table
plt.legend(loc='upper right')

plt.savefig("novice_final.png", dpi=300, bbox_inches='tight')