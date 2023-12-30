"""

  Title: Plotting a Simple Line Graph  
  Author: Eric Matthes
  Date: 12/29/2023
  Description: "Let's plot a simple line graph using Matplotlib and then customize 
  it to create more informative data visualization."

"""


import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()


ax.plot(input_values, squares, linewidth=3)

ax.set_title("Squares Numbers", fontsize=24)

ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()



