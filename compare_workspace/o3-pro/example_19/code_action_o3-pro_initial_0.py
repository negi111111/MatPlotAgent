import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. Raw Data (exactly as provided)
# ------------------------------------------------------------------
sales_data = [
    [120, 95, 130, 85, 100],   # Apples
    [90, 115, 80, 105, 95],    # Oranges
    [75, 80, 85, 70, 90],      # Bananas
    [65, 70, 60, 75, 80],      # Grapes
    [55, 60, 65, 50, 55]       # Berries
]
fruit_labels  = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']
region_labels = ['North', 'South', 'East', 'West', 'Central']

# ------------------------------------------------------------------
# 2. Convert to NumPy array for easier math
# ------------------------------------------------------------------
data = np.array(sales_data)  # shape = (5 fruits, 5 regions)

# ------------------------------------------------------------------
# 3. Choose pastel colors for the fruit stacks
# ------------------------------------------------------------------
pastel      = plt.cm.Pastel1.colors
bar_colors  = pastel[:5]      # five gentle pastel shades

# ------------------------------------------------------------------
# 4. Prepare the figure and axis
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

# ------------------------------------------------------------------
# 5. Draw stacked bars
# ------------------------------------------------------------------
bar_width          = 0.6
x                  = np.arange(len(region_labels))  # 0 … 4
cumulative_bottom  = np.zeros(len(region_labels))   # starting baseline

for i, row in enumerate(data):
    ax.bar(
        x,
        row,
        width=bar_width,
        bottom=cumulative_bottom,
        color=bar_colors[i],
        label=fruit_labels[i]
    )
    cumulative_bottom += row

# ------------------------------------------------------------------
# 6. Configure axes
# ------------------------------------------------------------------
ax.set_xticks(x)
ax.set_xticklabels(region_labels)
ax.set_xlabel('')  # intentionally left blank
ax.set_ylabel('Sales (Hundreds)')
ax.set_title('Sales by Region')
ax.set_ylim(0, cumulative_bottom.max() * 1.10)  # little head-room for annotations

# ------------------------------------------------------------------
# 7. Annotate cumulative totals for each region
# ------------------------------------------------------------------
totals = data.sum(axis=0)
for idx, total in enumerate(totals):
    ax.text(
        x[idx],
        total + 2,                 # 2 units above bar top
        f'{total}',
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold'
    )

# ------------------------------------------------------------------
# 8. Build the underlying table
# ------------------------------------------------------------------
# Convert sales numbers to hundreds → decimal with two places
table_data     = np.round(data / 100.0, 2)
table_strings  = [[f'{val:.2f}' for val in row] for row in table_data]

# Match cell colours with bar colours (row-wise)
row_colors = [[bar_colors[i]] * len(region_labels) for i in range(len(fruit_labels))]

table = ax.table(
    cellText=table_strings,
    rowLabels=fruit_labels,
    colLabels=region_labels,
    cellColours=row_colors,
    rowLoc='left',
    colLoc='center',
    loc='bottom'
)

# Make the table text smaller and adjust spacing
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.2)  # widen columns a bit, increase row height

# ------------------------------------------------------------------
# 9. Adjust layout so chart and table don’t overlap
# ------------------------------------------------------------------
fig.tight_layout(rect=[0, 0.2, 1, 0.95])  # reserve bottom 20% for table, top 5% for title

# ------------------------------------------------------------------
# 10. Optional: external legend (table already acts as a legend)
# ------------------------------------------------------------------
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)

# ------------------------------------------------------------------
# 11. Save the figure (required)
# ------------------------------------------------------------------
plt.savefig("novice.png")