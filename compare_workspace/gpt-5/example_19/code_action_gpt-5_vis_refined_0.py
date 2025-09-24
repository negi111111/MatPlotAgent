import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Define the sales data
sales_data = [
    [120, 95, 130, 85, 100],  # Apples
    [90, 115, 80, 105, 95],   # Oranges
    [75, 80, 85, 70, 90],     # Bananas
    [65, 70, 60, 75, 80],     # Grapes
    [55, 60, 65, 50, 55]      # Berries
]

# Regions and colors (soft shades)
regions = ['North', 'South', 'East', 'West', 'Central']
colors = ['#B3CDE0', '#FBB4AE', '#C2DFFF', '#FCEBB1', '#FFB3BA']  # Soft shades

# Convert sales to numpy array and scale to hundreds for plotting consistency
sales_data = np.array(sales_data, dtype=float)
sales_hundreds = sales_data / 100.0

# Create the stacked bar chart
plt.figure(figsize=(10, 7))
plt.bar(regions, sales_hundreds[0], color=colors[0], label='Apples')
labels_for_rest = ['Oranges', 'Bananas', 'Grapes', 'Berries']
for i in range(1, sales_hundreds.shape[0]):
    plt.bar(
        regions,
        sales_hundreds[i],
        bottom=sales_hundreds[:i].sum(axis=0),
        color=colors[i],
        label=labels_for_rest[i - 1]
    )

# Add cumulative sales values on top of each stacked bar (in hundreds)
cumulative_sales = sales_hundreds.sum(axis=0)
# Ensure text has space above bars
plt.ylim(0, cumulative_sales.max() * 1.15)
for i, value in enumerate(cumulative_sales):
    plt.text(i, value + 0.05, f'{value:.2f}', ha='center', va='bottom', fontsize=9)

# Title and axis labels
plt.title('Sales by Region')
plt.ylabel('Sales (hundreds)')
plt.xticks([])  # Unlabeled x-axis

# Create the table below the chart (values in hundreds)
table_data = sales_hundreds.round(2)
cell_colours = np.array([[colors[i]] * len(regions) for i in range(sales_hundreds.shape[0])])
plt.table(
    cellText=table_data,
    colLabels=regions,
    rowLabels=['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries'],
    cellLoc='center',
    loc='bottom',
    cellColours=cell_colours,
    bbox=[0.0, -0.35, 1.0, 0.3]
)

# Adjust layout to make space for the table
plt.subplots_adjust(bottom=0.3)

# Save exactly one PNG
plt.savefig('novice_final.png', bbox_inches='tight')