"""

  Title: Creating the RandomWalk Class  
  Author: Eric Matthes
  Date: 01/02/2024
  Description: "...code to plot all the points in the walk."

"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk 

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()