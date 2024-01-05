"""

  Title: Analyzing the Results  
  Author: Eric Matthes
  Date: 01/04/2024
  Description: "We'll analyze the results of rolling one D6 by counting how many 
  times we roll each number:"

"""

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list. 
results = []

for roll_num in range(1000):
  result = die.roll()
  results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
  frequency = results.count(value)
  frequencies.append(frequency)

print(frequencies)

"""

  "Because we're no longer printing the results, we can increase the number of 
  simulated rolls to 1000. To analyze the rolls, we create the empty list frequencies 
  to store the number of times each value is rolled. We then generate all the 
  possible reults we could get; in this example, that's all the numbers 
  from 1 to however many sides die has. We loop through the possible values, 
  count how many times each number appears in results, and then append this 
  value to frequencies. We print this list before making a visualization:"

  [166, 158, 187, 168, 154, 167]

"""



