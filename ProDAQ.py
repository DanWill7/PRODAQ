# UDFs for PRODAQ the application to be used in main.py
# Author: Daniel Williams
# Date Created: 12/5/2020 5:42PM

import random as r

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import lines, style


def live_plot(filepath: str):
    # This function takes in a file locaction to read data and create a live plot feed.
    style.use('fivethirtyeight')

    # createing the number of plots layout and color of layout
    fig, axs = plt.subplots(1, 2, facecolor=(.18, .31, .31))
    fig.set_size_inches(18.5, 10.5)
    # set figure size

    fig.suptitle('Motor Chamber Performance Live Feed', color='0.7')
    # creating figure title and color for all subplots

    def animate(i):
        """Function used to live update the plot. The function constantly updates and is reading the txt file for an update to the data set stored.

        Args:
            i : Variable used to iterate upon for the graph updating.
        """

        # opens the desired file and reads the data
        graph_data = open(filepath, 'r').read()
        # splits the data at the newline character to get indiviual ordered pairs
        lines = graph_data.split('\n')
        # initializing empty lists to append to later
        xs = []
        ys = []
        ts = []
        # looping through each value in txt file to add to the list
        for line in lines:
            if len(line) > 1:
                x, y, t = line.split(',')
                # splits all the lines into their respective pressure, thrust and time columns
                xs.append(float(x))
                ys.append(float(y))
                ts.append(float(t))
        # line Thickness
        width = 1
        # Below clears the plots for the updated plotting and sets the format of the individual plots and colros
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

    # Runs the animate UDF at a sample rate to update the plots in the figure
    ani = animation.FuncAnimation(fig, animate, interval=100)

    # Makes the figure maximized in the window
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    # displays the figure
    plt.show()

    return
