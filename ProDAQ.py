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

    
    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(18.5, 10.5)

    def animate(i):

        graph_data = open(filepath, 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        ts = []
        for line in lines:
            if len(line) > 1:
                x, y, t = line.split(',')
                xs.append(float(x))
                ys.append(float(y))
                ts.append(float(t))

        axs[0].clear()
        axs[1].clear()
        axs[1].plot(ts, ys, color='green')
        axs[0].plot(ts, xs, color='red')
        axs[0].set_xlabel("Time (Seconds)")
        axs[0].set_ylabel("Pressure (PSIA)")
        axs[1].set_xlabel("Time (Seconds)")
        axs[1].set_ylabel("Thrust (LBS)")
        #fig.tight_layout()
        #fig = plt.gcf()
        

    ani = animation.FuncAnimation(fig, animate, interval=50)
    plt.show()

    return
