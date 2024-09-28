import matplotlib.pyplot as plt
import numpy as np
import random
import json

ax = plt.figure().add_subplot(projection='3d')

with open('data/data_slimy.json') as json_file:
    DATA_SLIMY = json.load(json_file)
with open('data/data_bat.json') as json_file:
    DATA_BAT = json.load(json_file)

DATA_SECTION_SLIMY = int(len(DATA_SLIMY) / 3)
print(len(DATA_SLIMY))
DATA_SECTION_BAT = int(len(DATA_BAT) / 3)
print(len(DATA_BAT
          ))

slimy_cycle = np.array(DATA_SLIMY[:DATA_SECTION_SLIMY])
slimy_speed = np.array(DATA_SLIMY[DATA_SECTION_SLIMY:DATA_SECTION_SLIMY * 2])
slimy_vision = np.array(DATA_SLIMY[DATA_SECTION_SLIMY * 2:])

bat_cycle = np.array(DATA_BAT[:DATA_SECTION_BAT])
bat_speed = np.array(DATA_BAT[DATA_SECTION_BAT:DATA_SECTION_BAT * 2])
bat_vision = np.array(DATA_BAT[DATA_SECTION_BAT * 2:])


def hist_plot(speed, vision, cycle, info_plus=False):
    # proposition
    plt.hist2d(cycle, speed)
    plt.xlabel("cycle")
    plt.ylabel("speed")
    plt.show()
    plt.hist2d(cycle, vision)
    plt.xlabel("cycle")
    plt.ylabel("vision")
    plt.show()
    plt.hist2d(speed, vision)
    plt.xlabel("speed")
    plt.ylabel("vision")
    plt.show()

    # the most value
    if info_plus:
        plt.hist2d(speed, speed)
        plt.xlabel("speed")
        plt.ylabel("speed")
        plt.show()
        plt.hist2d(vision, vision)
        plt.xlabel("vision")
        plt.ylabel("vision")
        plt.show()
        plt.hist2d(cycle, cycle)
        plt.xlabel("cycle")
        plt.ylabel("cycle")
        plt.show()


def scatter3d(cycle, vision, speed):
    ax.scatter(cycle, vision, speed)
    plt.xlabel("cycle")
    plt.ylabel("vision")
    plt.show()


# dotted_plot(Z, X)
scatter3d(bat_cycle, bat_vision, bat_speed)
hist_plot(bat_speed, bat_vision, bat_cycle, True)
scatter3d(slimy_cycle, slimy_vision, slimy_speed)
hist_plot(slimy_speed, slimy_vision, slimy_cycle, True)

