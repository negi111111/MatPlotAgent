import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1) Import libraries and prepare the data
fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']
regions = ['North', 'South', 'East', 'West', 'Central']
sales_data = [
    [120, 95, 130, 85, 100],  # Apples
    [90, 115, 80, 105, 95],   # Oranges
    [75, 80, 85, 70, 90],     # Bananas
    [65, 70, 60, 75, 80],     # Grapes
    [55, 60, 65, 50, 55]      # Berries
]
data = np.array(sales_data, dtype=float)

# Convert to "hundreds" for plotting and table
sales_data_hundreds = data / 100.0  # shape (5 fruits, 5 regions)

# 2) Create the figure and axes
fig, (ax, ax_table) = plt.subplots(
    2, 1,
    figsize=(10, 8),
    gridspec_kw={'height_ratios': [3, 2]}
)

# 3) Colors (soft shades)
colors = plt.cm.Pastel1(np.linspace(0.15, 0.85, len(fruits)))

# 4) Stacked bar chart
x = np.arange(len(regions))
bar_width = 0.7
bottom = np.zeros(len(regions))

for i, fruit in enumerate(fruits):
    ax.bar(
        x,
        sales_data_hundreds[i],
        width=bar_width,
        bottom=bottom,
        color=colors[i],
        edgecolor='white'
    )
    bottom += sales_data_hundreds[i]

# 5) Axis formatting
ax.set_title('Sales by Region')
ax.set_ylabel('Sales (hundreds)')
# Keep x-axis unlabeled (no tick labels or tick marks)
ax.set_xticks(x)  # positions defined, but we hide labels/marks
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

# 6) Cumulative labels on top of each stacked bar
totals_hundreds = sales_data_hundreds.sum(axis=0)
ax.set_ylim(0, totals_hundreds.max() * 1.10)

for xi, total in zip(x, totals_hundreds):
    ax.text(
        xi,
        total + 0.02,
        f"{total:.2f}",
        ha='center',
        va='bottom',
        fontsize=10
    )

# 7) Table below the chart
ax_table.axis('off')

# Prepare table text formatted to two decimals
cell_text = [[f"{val:.2f}" for val in row] for row in sales_data_hundreds]

table = ax_table.table(
    cellText=cell_text,
    rowLabels=fruits,
    colLabels=regions,
    rowColours=colors,
    cellLoc='center',
    loc='center'
)

# Improve table readability
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.3)

# 8) Layout adjustments and save to file
plt.subplots_adjust(hspace=0.25, top=0.90)
plt.savefig("novice.png")