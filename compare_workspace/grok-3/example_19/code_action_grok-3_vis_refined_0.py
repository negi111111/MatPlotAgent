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

# Set up regions and colors
regions = ['North', 'South', 'East', 'West', 'Central']
colors = ['#FF9999', '#FFCC99', '#FFFF99', '#CCFF99', '#99CCFF']  # Soft shades

# Convert sales data to numpy array for easier manipulation
sales_data = np.array(sales_data)
cumulative_sales = np.zeros(len(regions))

# Create stacked bar chart
for i in range(len(sales_data)):
    plt.bar(regions, sales_data[i], bottom=cumulative_sales, color=colors[i], label=f'Fruit {i+1}')
    cumulative_sales += sales_data[i]

# Add cumulative sales values on top of each bar
for i, total in enumerate(cumulative_sales):
    plt.text(i, total + 10, str(total), ha='center', va='bottom')

# Set y-axis label and title
plt.ylabel('Sales (Hundreds)')
plt.title('Sales by Region')

# Create a table below the chart
cell_text = []
for i in range(len(sales_data)):
    cell_text.append([f'{value/100:.2f}' for value in sales_data[i]])

plt.table(cellText=cell_text, colLabels=regions, rowLabels=['Apples', 'Oranges', 'Bananas', 'Grapes', 'Berries'],
          cellLoc='center', loc='bottom', bbox=[0.1, -0.5, 0.8, 0.4])

# Adjust layout to ensure visibility of chart and table
plt.subplots_adjust(bottom=0.3)

# Save the plot to a PNG file
plt.savefig('novice_final.png', bbox_inches='tight')