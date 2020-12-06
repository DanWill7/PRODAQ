# File uised to simulated measured pressures and thrust sensor outputs
# Author: Daniel Williams
# Date Created: 12/5/2020 7:20PM

import random as r
import time

file = open("test.txt", "w")
file.close()

while(True):
    time.sleep(.20)

    num1 = str(round(r.uniform(1, 10000)))
    num2 = str(round(r.uniform(1, 10000)))
    string = num1 + "," + num2 + "\n"
    file = open("test.txt", 'a')
    file.write(string)
    print("iteration")
done
