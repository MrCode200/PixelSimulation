import matplotlib.pyplot as plt
import numpy as np
import random
import json

ax = plt.figure().add_subplot(projection='3d')

with open('data.json') as json_file:
    DATA = json.load(json_file)

DATA_SECTION = int(len(DATA) / 3)
print(len(DATA))


Z = np.array(DATA[:DATA_SECTION])
X = np.array(DATA[DATA_SECTION:DATA_SECTION * 2])
Y = np.array(DATA[DATA_SECTION * 2:])

def bar_plot(x, y):
    plt.xlabel("SPEED")
    plt.ylabel("VISION_R")
    plt.bar(x, y)
    plt.show()


def hist_plot():
    plt.hist2d(Z, X)
    plt.show()
    plt.hist2d(Z, Y)
    plt.show()
    plt.hist2d(X, Y)


def Scatter3d(z, x, y):
    ax.scatter(x, y, z)
    plt.show()


# dotted_plot(Z, X)
Scatter3d(Z, X, Y)
hist_plot()

plt.show()
plt.hist2d(X,X)
plt.show()
plt.hist2d(Y,Y)
plt.show()
plt.hist2d(Z,Z)
plt.show()

