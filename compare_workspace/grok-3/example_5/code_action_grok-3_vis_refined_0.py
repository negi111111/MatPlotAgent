import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Data for pie chart
fruit_labels = ['Apples', 'Oranges', 'Bananas']
fruit_sizes = [35, 45, 20]

# Data for stacked bar chart
age_groups = ['<18', '18-30', '30-50', '>50']
apple_preferences = [25, 40, 20, 15]

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Pie chart
wedges, texts, autotexts = ax1.pie(fruit_sizes, labels=fruit_labels, autopct='%1.1f%%', startangle=90, explode=(0.1, 0, 0))
ax1.set_title('Fruit Distribution in Basket')

# Stacked bar chart
ax2.bar(age_groups, apple_preferences, color=['red', 'orange', 'yellow', 'lightyellow'])
ax2.set_title('Apple Preference by Age Group')
ax2.set_ylabel('Percentage of People Favoring Apples')
ax2.set_ylim(0, 100)

# Adjust layout
plt.subplots_adjust(wspace=0.5)

# Add legend
ax1.legend(wedges, fruit_labels, title="Fruits", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Save the plot
plt.savefig('novice_final.png', bbox_inches='tight')