"""
    Plotting Cubic Numbers, Option 2 for Lab 4
    Sarah Estes
    Program that uses matplotlibs to plot cubic numbers
    11/17/2026
"""

import matplotlib.pyplot as plt

def first_5():
    input_values = [1, 2, 3, 4, 5]
    cubes = [1, 8, 27, 64, 125]

    fig, ax = plt.subplots()
    ax.plot(input_values, cubes)

    ax.set_title("First 5 Cubes", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cube of Value", fontsize=14)

    # plt.show()
    plt.savefig("5cubes.png")

def first_5000():
    input_values = list(range(1, 5001))
    cubes = []

    for value in input_values:
        cubed_value = value ** 3
        cubes.append(cubed_value)

    fig, ax = plt.subplots()
    ax.plot(input_values, cubes)

    ax.set_title("First 5000 Cubes", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cube of Value", fontsize=14)

    # plt.show()
    plt.savefig("5000cubes.png")

first_5()
first_5000()