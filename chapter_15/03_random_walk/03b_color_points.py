"""

  Title: Generating Multiple Random Walks  
  Author: Eric Matthes
  Date: 01/02/2024
  Description: "We'll use a colormap to show the order of the points in the walk, 
  and remove the black outline from each dot so the color of the dots will be clearer. 
  To color the points according to their position in the walk, we pass 
  the c argument a list containing the position of each point. Because the points 
  are plotted in order, this list just contains the numbers from 0 to 4,999:"

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
  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break