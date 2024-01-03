"""

  Title: Generating Multiple Random Walks  
  Author: Eric Matthes
  Date: 01/02/2024
  Description: "In addition to coloring points to show their position along the 
  walk, it would be useful to see exactly where each walk begins and ends. To do 
  so, we can plot the first and last points individually after the main series 
  has been plotted. We'll make the end points larger and color them differently 
  to make them stand out:"

"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk 

# Keep making new walks, as long as the program is active.
while True: 


  # Make a random walk.
  rw = RandomWalk()
  rw.fill_walk()

  # Plot the points in the walk.
  plt.style.use('classic')
  fig, ax = plt.subplots()

  # Color the points.
  point_numbers = range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)


  ax.set_aspect('equal')


  # Emphasize the first and last points. 
  ax.scatter(0, 0, c='green', edgecolors='none', s=100)
  ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)


  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break