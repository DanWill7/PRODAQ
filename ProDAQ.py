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

    fig, axs = plt.subplots(1, 2, facecolor=(.18, .31, .31))
    fig.set_size_inches(18.5, 10.5)
    fig.suptitle('Motor Chamber Performance Live Feed', color='0.7')

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

        width = 1
        axs[0].clear()
        axs[1].clear()
        axs[0].set_facecolor('#eafff5')
        axs[1].set_facecolor('#eafff5')
        axs[1].plot(ts, ys, 'xkcd:crimson', linewidth=width)
        axs[0].plot(ts, xs, 'xkcd:crimson', linewidth=width)
        axs[0].set_xlabel("Time (Seconds)", color='c')
        axs[0].set_ylabel("Pressure (PSIA)", color='peachpuff')
        axs[1].set_xlabel("Time (Seconds)", color='c')
        axs[1].set_ylabel("Thrust (LBS)", color='peachpuff')
        axs[0].tick_params(labelcolor='tab:orange')
        axs[1].tick_params(labelcolor='tab:orange')

    ani = animation.FuncAnimation(fig, animate, interval=100)
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()

    return
