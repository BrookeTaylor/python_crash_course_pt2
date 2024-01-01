"""

  Title: Changing the Label Type and Line Thickness  
  Author: Eric Matthes
  Date: 12/29/2023
  Description: "We'll use a few of the available customizations to improve this 
  plot's readability. Let's start by adding a title and labeling the axes:"

"""

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()


# "The linewidth parameter controls the thickness of the line that plot() generates."
ax.plot(squares, linewidth=3)


"""
  "Once a plot has been generated,there are many methods available to modify the 
  plot before it's presented. The set_title() method sets an overall title for 
  the chart. The fontsize parameters, which appear repeatedly throughout the code, 
  control the size of the text in various elements on the chart."
"""
ax.set_title("Squares Numbers", fontsize=24)


# "The set_xlabel() and set_ylabel() methods allow you to set a title for each 
# of the axes, and the method tick_params() styles the tick marks."
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# "Here tick_params() sets the font size of the tick mark labels to 14 on both axes."
ax.tick_params(labelsize=14)

plt.show()



