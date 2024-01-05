"""

  Title: Rolling Two Dice  
  Author: Eric Matthes
  Date: 01/04/2024
  Description: "Rolling two dice results in larger numbers and a different 
  distribution of results. Let's modify our code to create two D6 dice to simulate 
  the way we roll a pair of dice. Each time we roll the pair, we'll add the two 
  numbers and store the sum in results."

"""

import plotly.express as px

from die import Die

# Create two D6 dice.
die_01 = Die()
die_02 = Die()

# Make some rolls, and store results in a list. 
results = []

for roll_num in range(1000):
  result = die_01.roll() + die_02.roll()
  results.append(result)

# Analyze the results.
frequencies = []
max_result = die_01.num_sides + die_02.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
  frequency = results.count(value)
  frequencies.append(frequency)


# Visualize the results.
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

