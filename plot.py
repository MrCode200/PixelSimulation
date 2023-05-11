import matplotlib.pyplot as plt
import numpy as np
import random
import json

with open('data.json') as json_file:
    DATA = json.load(json_file)

X = np.array(DATA[0:int(len(DATA) / 2)])
Y = np.array(DATA[int(len(DATA) / 2):])

print(np.count_nonzero(X == 1))
print(np.count_nonzero(X == 2))
print(np.count_nonzero(X == 3))
print(np.count_nonzero(Y == 45))
print(np.count_nonzero(Y == 50))
print(np.count_nonzero(Y == 55))
print(np.count_nonzero(Y == 60))
print(np.count_nonzero(Y == 65))
print(np.count_nonzero(Y == 70))
print(np.count_nonzero(Y == 75))



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


#bar_plot(X, Y)
#dotted_plot(X, Y)
