import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Define sales data
sales_data = [
    [120, 95, 130, 85, 100],  # Apples
    [90, 115, 80, 105, 95],   # Oranges
    [75, 80, 85, 70, 90],     # Bananas
    [65, 70, 60, 75, 80],     # Grapes
    [55, 60, 65, 50, 55]      # Berries
]

regions = ['North', 'South', 'East', 'West', 'Central']
fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']
colors = ['#FF9999', '#FFCC99', '#FFFF99', '#CCFF99', '#99CCFF']  # Soft shades

# Convert to numpy array for easier manipulation
sales_array = np.array(sales_data)
cumulative_sales = np.zeros(len(regions))

# Create stacked bar chart
for i, fruit in enumerate(fruits):
    plt.bar(regions,
            sales_array[i],
            bottom=cumulative_sales,
            color=colors[i],
            label=fruit)
    cumulative_sales += sales_array[i]

# Annotate cumulative totals on top of each bar
for idx, total in enumerate(cumulative_sales):
    plt.text(idx, total + 10, str(int(total)), ha='center', va='bottom')

# Labels and title
plt.ylabel('Sales (hundreds)')
plt.xticks([])  # Remove x-axis labels
plt.title('Sales by Region')

# Create table below the plot
cell_text = [[f"{value/100:.2f}" for value in row] for row in sales_array]
plt.table(
    cellText=cell_text,
    colLabels=regions,
    rowLabels=fruits,
    rowColours=colors,
    cellLoc='center',
    loc='bottom',
    bbox=[0.1, -0.5, 0.8, 0.4]
)

# Adjust layout to make room for the table
plt.subplots_adjust(bottom=0.3)

# Save the figure
plt.savefig('novice_final.png', bbox_inches='tight')