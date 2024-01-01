"""

  Title: Saving Your Plots Automatically  
  Author: Eric Matthes
  Date: 12/31/2023
  Description: "If you want to save the plot to a file instead of showing it in 
  the Matplotlib viewer, you can use plt.savefig() instead of plt.show():"

"""


import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1_100_000])

ax.ticklabel_format(style='plain')

plt.savefig('02f_saving_plots.png', bbox_inches='tight')