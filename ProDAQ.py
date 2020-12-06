# UDFs for PRODAQ the application to be used in main.py
# Author: Daniel Williams
# Date Created: 12/5/2020 5:42PM

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import lines, style
import random as r


def live_plot(filepath: str):
    # This function takes in a file locaction to read data and create a live plot feed.
    style.use('fivethirtyeight')

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(i):

        graph_data = open(filepath, 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(float(x))
                ys.append(float(y))

        ax1.clear()
        ax1.set_xlabel("Pressure")
        ax1.set_ylabel("Thrust")
        ax1.plot(xs, ys)

    ani = animation.FuncAnimation(fig, animate, interval=50)
    fig.tight_layout()
    fig.set_size_inches(18.5, 10.5)
    fig = plt.gcf()
    plt.show()

    return
