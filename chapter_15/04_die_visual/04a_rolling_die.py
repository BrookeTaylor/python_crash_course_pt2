"""

  Title: Creating the Die Class  
  Author: Eric Matthes
  Date: 01/04/2024
  Description: "Before creating a visualization based on the Die class, let's 
  roll a D6, print the results, and check that the results look reasonable:"

"""

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list. 
results = []

for roll_num in range(100):
  result = die.roll()
  results.append(result)

print(results)



"""

  "we create an instance of Die with the default six sides. Then we roll the 
  die 100 times and store the results of each roll in the list results. Here's 
  a sample set of results:"

  [6, 2, 3, 6, 5, 4, 2, 5, 5, 1, 2, 6, 1, 2, 2, 1, 6, 2, 6, 3, 4, 5, 3, 4, 4, 3, 
  4, 5, 5, 6, 1, 4, 5, 1, 4, 5, 6, 5, 5, 2, 5, 4, 1, 3, 2, 5, 3, 2, 5, 5, 5, 6, 
  1, 5, 1, 4, 2, 4, 1, 2, 4, 4, 2, 3, 5, 5, 6, 2, 5, 1, 1, 5, 3, 1, 1, 2, 5, 6, 
  5, 2, 5, 5, 2, 4, 3, 3, 2, 3, 3, 5, 3, 3, 3, 6, 6, 4, 1, 2, 5, 6]

  A quick scan of these results shows that the Die class seems to be working. We 
  see the values 1 and 6, so we know the smallest and largest possible values 
  are being returned, and because we don't see 0 or 7, we know all the results 
  are in the appropriate range. We also see each number from 1 through 6, which 
  indicates that all possible outcomes are represented. 

"""
