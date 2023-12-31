"""

  Title: Creating the Die Class  
  Author: Eric Matthes
  Date: 01/04/2024
  Description: "We'll create the following Die class to simulate the roll 
  of one die:"

"""

from random import randint

class Die:
  """ A class representing a single die."""

  def __init__(self, num_sides=6):
    """Assume a six-sided die."""
    self.num_sides = num_sides

  def roll(self):
    """Return a random value between 1 and number of sides."""
    return randint(1, self.num_sides)
    

"""

  "The __init__() method takes one optional argument. With the Die class, when 
  an instance of our die is created, the number of sides will be six if no argument 
  is included. If an argument is included, that value will set the number of sides 
  on the die. 

  The roll() method uses the randint() function to return a random number between 
  1 and the number of sides. This function can return the starting value (1), 
  the ending value (num_sides), or any integer between the two.

"""