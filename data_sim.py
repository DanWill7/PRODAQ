# File uised to simulated measured pressures and thrust sensor outputs
# Author: Daniel Williams
# Date Created: 12/5/2020 7:20PM

import random as r
import time
import pandas as pd

df = pd.read_csv("Test Data\Pressure thrust data1.csv")


file = open("test.txt", "w")
file.close()

counter = 0
while(counter < df.shape[0]):
    time_ellapsed = float(df.iloc[df.shape[0] - 1, [2]])
    sample_rate = time_ellapsed/(df.shape[0]-1)
    time.sleep(sample_rate)

    num1 = float(df.iloc[counter, [0]])
    num2 = float(df.iloc[counter, [1]])
    string = str(num1) + "," + str(num2) + "\n"
    file = open("test.txt", 'a')
    file.write(string)
    counter = counter + 1
    print("Iteration " + str(counter))
