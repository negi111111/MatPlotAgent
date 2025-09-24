import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Data for pie chart
fruit_labels = ['Apples', 'Oranges', 'Bananas']
fruit_sizes = [35, 45, 20]
fruit_explode = (0.1, 0, 0)  # explode the Apples slice

# Data for stacked bar chart
age_groups = ['Under 18', '18-30', '30-50', 'Over 50']
favoring_apples = [25, 40, 20, 15]

# Create side-by-side subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Pie chart on the first axis
ax1.pie(
    fruit_sizes,
    explode=fruit_explode,
    labels=fruit_labels,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops=dict(edgecolor='white')
)
ax1.axis('equal')  # Draw as a circle
ax1.set_title('Fruit Distribution in Basket')

# Bar chart on the second axis
x = np.arange(len(age_groups))
bars = ax2.bar(
    x,
    favoring_apples,
    color='skyblue',
    edgecolor='black'
)
ax2.set_xticks(x)
ax2.set_xticklabels(age_groups)
ax2.set_ylabel('Percentage (%)')
ax2.set_title('People Favoring Apples by Age Group')

# Compute the pie chart center in figure coordinates
# The default pie is centered at data (0,0) on ax1
pie_center_data = (0, 0)
pie_center_disp = ax1.transData.transform(pie_center_data)
pie_center_fig = fig.transFigure.inverted().transform(pie_center_disp)

# Draw lines from the pie (Apples slice) to each bar top
for bar in bars:
    bar_center = bar.get_x() + bar.get_width() / 2
    bar_top = bar.get_height()
    bar_disp = ax2.transData.transform((bar_center, bar_top))
    bar_fig = fig.transFigure.inverted().transform(bar_disp)
    fig.annotate(
        '',
        xy=bar_fig,
        xytext=pie_center_fig,
        xycoords='figure fraction',
        textcoords='figure fraction',
        arrowprops=dict(arrowstyle='-', color='black', linewidth=1)
    )

# Adjust layout and save
plt.tight_layout()
plt.savefig("novice_final.png")