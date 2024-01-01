"""

  Title: Calculating Data Automatically  
  Author: Eric Matthes
  Date: 12/30/2023
  Description: "Writing lists by hand can be inefficient, especially when we have 
  many points. Rather than writing out each value, let's use a loop to do the 
  calculations for us."

"""

import matplotlib.pyplot as plt


# "We start with a range of x-values containing the numbers 1 through 1,000."
x_values = range(1, 1001)

# "Next, a list comprehension generates the y-values by looping through the 
# x_values (for x in x_values), squaring each number (x**2), and assigning the 
# results to y_values."
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()


# "We then pass the input and output lists to scatter()."
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


"""
  "Before showing the plot, we use the axis() method to specify the range of 
  each axis. The axis() method requires four values: the minimum and maximum values 
  for the x-axis and the y-axis. Here, we run the x-axis from 0 to 1,100 and the 
  y-axis from 0 to 1,100,000."
"""
# "Before showing the plot, we use the axis() method to specify the range of 
# each axis."
ax.axis([0, 1100, 0, 1_100_000])

plt.show()