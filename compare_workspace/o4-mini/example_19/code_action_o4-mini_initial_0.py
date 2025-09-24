import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 1. Define data and labels
regions = ['North', 'South', 'East', 'West', 'Central']
fruits  = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']
sales_data = [
    [120, 95, 130, 85, 100],  # Apples
    [90, 115, 80, 105, 95],   # Oranges
    [75, 80, 85, 70, 90],     # Bananas
    [65, 70, 60, 75, 80],     # Grapes
    [55, 60, 65, 50, 55]      # Berries
]

# 2. Convert to NumPy and compute cumulative sums
data = np.array(sales_data)           # shape (5 fruits, 5 regions)
cum_data = np.cumsum(data, axis=0)    # running totals down each column
totals = cum_data[-1, :]              # total sales per region

# 3. Plot parameters
x = np.arange(len(regions))           # [0,1,2,3,4]
colors = ['#ff9999', '#ffd580', '#c7e9c0', '#d0b0e0', '#b0cfe0']
bar_width = 0.6

# 4. Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# 5. Draw stacked bars
bottom = np.zeros(len(regions))
for fruit, row, col in zip(fruits, data, colors):
    ax.bar(
        x,
        row,
        bottom=bottom,
        color=col,
        width=bar_width,
        edgecolor='white',
        label=fruit
    )
    bottom += row

# 6. Configure axes and title
ax.set_ylabel('Sales (hundreds)')
ax.set_title('Sales by Region')
ax.set_xticks(x)
ax.set_xticklabels(regions)
ax.set_xlabel('')  # no x-axis label

# 7. Annotate cumulative totals
for idx, total in enumerate(totals):
    ax.text(
        idx,
        total + 3,      # small offset above bar
        str(total),
        ha='center',
        va='bottom',
        fontsize=10
    )

# 8. Prepare table data (values divided by 100, two decimals)
table_data = []
for row in data:
    formatted_row = [f"{val/100:.2f}" for val in row]
    table_data.append(formatted_row)

# 9. Add coloured table below the chart
the_table = ax.table(
    cellText=table_data,
    rowLabels=fruits,
    colLabels=regions,
    rowColours=colors,
    cellLoc='center',
    loc='bottom'
)
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.scale(1, 1.5)  # increase row height

# 10. Adjust layout to make space for the table
plt.subplots_adjust(left=0.1, bottom=0.25, right=0.95, top=0.9)

# 11. Save the figure
plt.savefig("novice.png")