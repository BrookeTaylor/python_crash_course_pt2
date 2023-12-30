"""

  Title: Plotting and Styling Individual Points with scatter()  
  Author: Eric Matthes
  Date: 12/29/2023
  Description: "Sometimes, it's useful to plot and style individual points based 
  on certain characteristics. For example, you might plot small values in one 
  color and larger values in a different color. You could also plot a large dataset 
  with one set of styling options and then emphasize individual points by re-plotting 
  them with different options."

"""

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels. 
ax.tick_params(labelsize=14)

plt.show()