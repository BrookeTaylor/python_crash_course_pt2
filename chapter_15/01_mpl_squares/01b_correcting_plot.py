"""

  Title: Correcting the Plot  
  Author: Eric Matthes
  Date: 12/29/2023
  Description: "When you give plot() a single sequence of numbers, it assumes the 
  first data point corresponds to an x-value of 0, but our first point corresponds 
  to an x-value of 1. We can override the default behavior by giving plot() both 
  the input and output values used to calculate the squares:"

"""


import matplotlib.pyplot as plt


"""
  "When you give plot() a single sequence of numbers, it assumes the first data 
  point corresponds to an x-value of 0, but our first point corresponds to 
  an x-value of 1."
"""
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()


ax.plot(input_values, squares, linewidth=3)

ax.set_title("Squares Numbers", fontsize=24)

ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()



