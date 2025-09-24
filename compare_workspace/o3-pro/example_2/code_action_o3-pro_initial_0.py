import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate the data
z = np.linspace(-5, 5, 400)   # 400 points between -5 and 5
w = z.copy()                  # w identical to z

# 2. Create a 3 × 3 grid of shared-axis subplots with no internal spacing
fig, ax = plt.subplots(
    nrows=3,
    ncols=3,
    sharex='col',
    sharey='row',
    figsize=(9, 9),
    gridspec_kw={'hspace': 0, 'wspace': 0}
)

# 3. Specify the (x, y, color) triplets for each panel
plots = [
    (w,          z,               None),      # 1
    (w,          z**3,            'blue'),    # 2
    (w + 1,     -z,               'yellow'),  # 3
    (w + 2,     -z**3,            'purple'),  # 4
    (w**2,       z**2,            'brown'),   # 5
    (w**2 + 1,  -z**2,            'pink'),    # 6
    (-w**2 + 2,  z**2,            'grey'),    # 7
    (-w**2 + 3, -z**2,            'black'),   # 8
    (-w,         z,               'white')    # 9
]

# 4. Plot each curve in its corresponding subplot
for axis, (xdata, ydata, colour) in zip(ax.flat, plots):
    if colour is None:
        axis.plot(xdata, ydata, linewidth=1.5)
    else:
        axis.plot(xdata, ydata, color=colour, linewidth=1.5)

# 5. Show tick labels only on the outer axes
for axis in ax.flat:
    axis.label_outer()

# 6. Overall title
fig.suptitle('Sharing x per column, y per row', fontsize=16)

# 7. Save the figure to disk
plt.savefig("novice.png", dpi=300)