"""

  Title: Rolling Two Dice  
  Author: Eric Matthes
  Date: 01/04/2024
  Description: "Let's create a six-sided die and a ten-sided die, and see what 
  happens when we roll them 50,000 times:"

"""

import plotly.express as px

from die import Die

# Create a D6 and a D10.
die_01 = Die()
die_02 = Die(10)

# Make some rolls, and store results in a list. 
results = []

for roll_num in range(50_000):
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
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

