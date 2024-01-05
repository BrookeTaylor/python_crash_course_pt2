"""

  Title: Rolling Two Dice  
  Author: Eric Matthes
  Date: 01/04/2024
  Description: "...While the default settings work well for most visualizations, 
  this chart would look better with all of the bars labeled. 
  
  Plotly has an update_layout() method that can be used to make a wide variety 
  of updates to a figure after it's been created."

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

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()

