"""

  Title: Generating Multiple Random Walks  
  Author: Eric Matthes
  Date: 01/02/2024
  Description: "Let's remove the axes in this plot so they don't distract from 
  the path of each walk."

"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk 

# Keep making new walks, as long as the program is active.
while True: 


  # Make a random walk.
  rw = RandomWalk(50_000)
  rw.fill_walk()

  # Plot the points in the walk.
  plt.style.use('classic')
  fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

  # Color the points.
  point_numbers = range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

  # Remove the axes.
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)


  ax.set_aspect('equal')


  # Emphasize the first and last points. 
  ax.scatter(0, 0, c='green', edgecolors='none', s=100)
  ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=1)


  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break