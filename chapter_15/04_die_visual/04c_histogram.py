"""

  Title: Making a Histogram  
  Author: Eric Matthes
  Date: 01/04/2024
  Description: "Now that we have the data we want, we can generate a 
  visualization in just a couple lines of code using Plotly Express:"

"""

# "We first import the plotly.express module, using the conventional alias px."
import plotly.express as px

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


# Visualize the results.
# "We then use the px.bar() function to create a bar graph. In the simplest use 
# of this function, we only need to pass a set of x-values and a set of y-values."
fig = px.bar(x=poss_results, y=frequencies)

# "The final line calls fig.show(), which tells Plotly to render the resulting 
# chart as an HTML file and open that file in a new browser tab."
fig.show()





