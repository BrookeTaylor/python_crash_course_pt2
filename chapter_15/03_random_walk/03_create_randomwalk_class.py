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
  """A class to generate random walks."""

  def __init__(self, num_points=5000):
    self.num_points = num_points

    # All walks start at (0, 0).
    self.x_values = [0]
    self.y_values = [0]