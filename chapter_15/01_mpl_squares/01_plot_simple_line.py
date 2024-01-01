"""

  Title: Plotting a Simple Line Graph  
  Author: Eric Matthes
  Date: 12/29/2023
  Description: "Let's plot a simple line graph using Matplotlib and then customize 
  it to create more informative data visualization."

"""

# "We first import the pyplot module using the alias plt so we don't have to type 
# type pyplot repeatedly. The pyplot module contains a number of functions that 
# help generate charts and plots."
import matplotlib.pyplot as plt


# "We create a list called squares to hold the data that we'll plot."
squares = [1, 4, 9, 16, 25]


"""
  "Then we follow another common Matplotlib convention by calling the subplots() 
  function. This function can generate one or more plots in the same figure. The 
  variable fig represents the entire figure, which is the collection of plots that 
  are generated."
"""
fig, ax = plt.subplots()


# "The variable ax represents a single plot in the figure; this is the variable 
# we'll use most of the time when defining and customizing a single plot."

# "We then use the plot() method, which tries to plot the data it's given in a 
# meaningful way."
ax.plot(squares)


# "The function plt.show() opens Matplotlib's viewer and displays the plot."
plt.show()




