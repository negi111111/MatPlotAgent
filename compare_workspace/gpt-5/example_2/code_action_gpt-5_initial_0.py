import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

# 1) Prepare base data arrays
w = np.linspace(-3, 3, 400)
z = np.linspace(-3, 3, 400)

# 2) Create a 3x3 subplot grid with shared axes per column/row and no spacing
fig, axes = plt.subplots(
    nrows=3,
    ncols=3,
    sharex='col',
    sharey='row',
    figsize=(8, 8),
    gridspec_kw={'wspace': 0, 'hspace': 0}
)

# 3) Set overall title
fig.suptitle('Sharing x per column, y per row', y=0.98)

# 4) Define what to plot in each subplot (y vs x, with color)
plots = [
    (z,            w,            None),       # 1. z against w
    (z**3,         w,            'blue'),     # 2. z**3 against w in blue
    (-z,           w + 1,        'yellow'),   # 3. -z against w + 1 in yellow
    (-(z**3),      w + 2,        'purple'),   # 4. -z**3 against w + 2 in purple
    (z**2,         w**2,         'brown'),    # 5. z**2 against w**2 in brown
    (-(z**2),      (w**2) + 1,   'pink'),     # 6. -z**2 against w**2 + 1 in pink
    (z**2,         -(w**2) + 2,  'grey'),     # 7. z**2 against -w**2 + 2 in grey
    (-(z**2),      -(w**2) + 3,  'black'),    # 8. -z**2 against -w**2 + 3 in black
    (z,            -w,           'white'),    # 9. z against -w in white
]

# 5) Plot into each subplot and show only outer labels
for ax, (y_vals, x_vals, color) in zip(axes.flat, plots):
    if color is not None:
        ax.plot(x_vals, y_vals, color=color)
    else:
        ax.plot(x_vals, y_vals)
    ax.label_outer()

# 6) Save the figure as a PNG
plt.savefig("novice.png")