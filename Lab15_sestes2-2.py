"""
    Plotting Cubic Numbers, Option 2 for Lab 4
    Sarah Estes
    Program that uses matplotlibs to plot cubic numbers
    11/17/2026
"""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()
ax.plot(input_values, cubes)

ax.set_title("First 5 Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

plt.savefig("5cubes.png")
plt.show()
