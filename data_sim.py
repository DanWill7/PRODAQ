# File uised to simulated measured pressures and thrust sensor outputs
# Author: Daniel Williams
# Date Created: 12/5/2020 7:20PM

import random as r
import time

import pandas as pd


df = pd.read_csv("Test Data\Pressure thrust data1.csv")
# read in the desired test file as pandas data frame

file = open("test.txt", "w")
file.close()
# clears file contents by opening the file and closing it immediately with no content

counter = 0
# tracks the number of iterations that have elapsed
while(counter < df.shape[0]):
    # runs for the length of the file/dataframe
    time_elapsed = float(df.iloc[df.shape[0] - 1, [2]])
    # finds the last time value in the dataframe to get the total time elapsed
    sample_rate = time_elapsed/(df.shape[0]-1)
    # creates sample rate by number of samples and total time elapsed
    time.sleep(sample_rate)
    # holds the program for the sample rate to write at the correcct speed of the sensor

    num1 = float(df.iloc[counter, [0]])
    num2 = float(df.iloc[counter, [1]])
    num3 = float(df.iloc[counter, [2]])
    # creating  the ordered pair from the dataframe
    string = str(num1) + "," + str(num2) + "," + str(num3) + "\n"
    # concenating the values to create a string line to be written to the end of the txt file
    file = open("test.txt", 'a')
    file.write(string)
    # opens and writes to the file

    counter = counter + 1
    # increases the iteration by 1

    print("Iteration " + str(counter))
    # prints to terminal the interation number
