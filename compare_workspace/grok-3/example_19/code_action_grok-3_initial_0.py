import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Define the sales data for each fruit across regions
sales_data = [
    [120, 95, 130, 85, 100],  # Apples
    [90, 115, 80, 105, 95],   # Oranges
    [75, 80, 85, 70, 90],     # Bananas
    [65, 70, 60, 75, 80],     # Grapes
    [55, 60, 65, 50, 55]      # Berries
]

# Define fruit names and region names
fruits = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries']
regions = ['North', 'South', 'East', 'West', 'Central']

# Convert sales data to numpy array for easier manipulation
sales_data = np.array(sales_data)

# Calculate total sales for each region (sum across fruits for each region)
total_sales_per_region = np.sum(sales_data, axis=0)

# Define soft colors for each fruit with high contrast
colors = ['#FF9999', '#FFCC99', '#FFFF99', '#CCFFCC', '#99CCFF']

# Create a figure and axis with a specific size to accommodate chart and table
fig, ax = plt.subplots(figsize=(10, 8))

# Define the x-axis positions for the bars
x = np.arange(len(regions))

# Initialize the bottom of the bars to zero for the first fruit
bottom = np.zeros(len(regions))

# Plot stacked bars for each fruit
for i, fruit in enumerate(fruits):
    ax.bar(x, sales_data[i], bottom=bottom, label=fruit, color=colors[i])
    bottom += sales_data[i]  # Update the bottom for the next stack

# Customize the chart
ax.set_title('Sales by Region', fontsize=14, pad=20)
ax.set_ylabel('Sales (Hundreds)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels([''] * len(regions))  # Remove x-axis labels as per requirement
ax.legend(title='Fruit', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add total sales value on top of each stacked bar
for i, total in enumerate(total_sales_per_region):
    ax.text(x[i], total, f'{total}', ha='center', va='bottom', fontsize=10)

# Format sales data for table (divide by 100 and format to 2 decimal places)
table_data = [[f'{val/100:.2f}' for val in row] for row in sales_data]
# Add row labels (fruit names) to the table data
table_data = [[fruit] + row for fruit, row in zip(fruits, table_data)]
# Define column labels for the table
col_labels = ['Fruit'] + regions

# Create a table below the chart
the_table = ax.table(cellText=table_data,
                     colLabels=col_labels,
                     loc='bottom',
                     cellLoc='center',
                     bbox=[0, -0.3, 1, 0.2])  # Adjust table position and size

# Color the table rows to match bar colors (skip header row)
for i, fruit in enumerate(fruits):
    for j in range(len(regions) + 1):  # +1 for the fruit name column
        the_table[(i+1, j)].set_facecolor(colors[i])  # i+1 to account for header row
        the_table[(i+1, j)].set_text_props(color='black')  # Ensure text is readable

# Adjust layout to ensure table and chart are visible
plt.subplots_adjust(bottom=0.3)

# Save the plot as a PNG file
plt.savefig("novice.png")