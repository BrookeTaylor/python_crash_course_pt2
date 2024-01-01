"""

  Title: Customizing Tick Labels  
  Author: Eric Matthes
  Date: 12/31/2023
  Description: "When the numbers on an axis get large enough, Matplotlib defaults 
  to scientific notation for tick labels. This is usually a good thing, because 
  larger numbers in plain notation take up a lot of unnecessary space on a visualization."

"""

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

"""
  "To change the color of the points, pass the argument color to scatter() with 
  the name of a color to use in quotation marks..."

  ax.scatter(x_values, y_values, color='red', s=10)

  "Values closer to 0 produce darker colors, and values closer to 1 produce
  lighter colors."
"""
ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1_100_000])

# "Almost every element of a chart is customizable, so you can tell Matplotlib 
# to keep using plain notation if you prefer:"
ax.ticklabel_format(style='plain')

plt.show()