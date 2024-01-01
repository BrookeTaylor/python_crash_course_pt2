"""

  Title: Using a Colormap  
  Author: Eric Matthes
  Date: 12/31/2023
  Description: "A colormap is a sequence of colors in a gradient that moves from 
  a starting to an ending color. In visualizations, colormaps are used to emphasize 
  patterns in data. For example, you might make low values a light color and 
  high values a darker color. Using colormap ensures that all points in the 
  visualization vary smoothly and accurately along a well-designed color scale.
  
  The pyplot module includes a set of built-in colormaps. To use one of these 
  colormaps, you need to specify how pyplot should assign a color to each point 
  in the dataset. Here's how to assign a color to each point, based on its y-value:"

"""

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()


"""
  "The c argument is similar to color, but it's used to associate a sequence of 
  values with a color mapping. We pass the list of y-values to c, and then tell 
  pyplot which colormap to use with the cmap argument. This code colors the points 
  with lower y-values light blue and the points with higher y-values dark blue."
"""
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 1100, 0, 1_100_000])

ax.ticklabel_format(style='plain')

plt.show()