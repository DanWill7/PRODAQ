# Main file to run UDFs for PRODAQ the application
# Author: Daniel Williams
# Date Created: 12/5/2020 5:42PM


import ProDAQ as daq


def main():
    filepath = "test.txt"
    # location of txt file with data
    daq.live_plot(filepath)
    # live plot the data


if __name__ == "__main__":
    main()
