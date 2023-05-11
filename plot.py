import matplotlib.pyplot as plt
import numpy as np
import random
import json

with open('data.json') as json_file:
    DATA = json.load(json_file)

X = np.array(DATA[0:int(len(DATA) / 2)])
Y = np.array(DATA[int(len(DATA) / 2):])


def bar_plot(x, y):
    plt.xlabel("SPEED")
    plt.ylabel("VISION_R")
    plt.bar(x, y)
    plt.show()


def dotted_plot(x, y):
    plt.xlabel("SPEED")
    plt.ylabel("VISION_R")
    plt.scatter(x, y, c='blue')
    plt.show()


def hist_plot(x, y):
    pass


bar_plot(X, Y)
dotted_plot(X, Y)
