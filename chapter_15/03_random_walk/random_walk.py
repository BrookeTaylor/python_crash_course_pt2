"""

  Title: Creating the RandomWalk Class  
  Author: Eric Matthes
  Date: 12/31/2023
  Description: "To create a random walk, we'll create a RandomWalk class, which 
  will make random decisions about which direction the walk should take. The 
  class needs three attributes: one variable to track the number of points in the 
  walk, and two lists to store the x- and y-coordinates of each point in the walk.
  
  We'll only need two methods of the RandomWalk class: the__init__() method and 
  fill_walk(), which will calculate the points in the walk. Let's start with the 
  __init__() method:"

"""

from random import choice

class RandomWalk: 
  # A class to generate random walks

  def __init__(self, num_points=5000):
    # Initialize attributes of a walk.
    self.num_points = num_points

    # All walks start at (0, 0).
    self.x_values = [0]
    self.y_values = [0]


  def fill_walk(self):
    # Calculate all the points in the walk.

    # Keep taking steps until the walk reaches the desired length.
    while len(self.x_values) < self.num_points:

      # Decide which direction to go, and how far to go. 
      x_direction = choice([1, -1])
      x_distance = choice([0, 1, 2, 3, 4])
      x_step = x_direction * x_distance

      y_direction = choice([1, -1])
      y_distance = choice([0, 1, 2, 3, 4])
      y_step = y_direction * y_distance

      # Reject moves that go nowhere.
      if x_step == 0 and y_step == 0:
        continue

      # Calculate the new position
      x = self.x_values[-1] + x_step
      y = self.y_values[-1] + y_step

      self.x_values.append(x)
      self.y_values.append(y)

