# PRODAQ

Author: Daniel Williams

Last Updated: 12/5/2020

Propulsion Tool to provide live data analysis of SRAD motor chamber pressurizations.

To begin coding in the repository follow the below setup procedure for WINDOWS.

Download Python 3 from <https://www.python.org/downloads/>

Make note of the install location for this download as you will likely neeed it later at various times. Also when installing select the option to add PYTHON to PATH.

Download Git Bash <https://git-scm.com/downloads>

Add to path environment variable.

Next step is to Download visual studio code from <https://code.visualstudio.com/download>

Open VS Code. Go to the "Terminal" tab. Select new terminal. In the newly opened you will notice in the command line the path to a folder location. Navigate, using the cd command, to the desired folder location on your computer you would like to store the github repository.

Next in the command line type git clone "https://github.com/dmw7/PRODAQ.git" to clone the existing remote repository.

Now you have the repository on your local machine in the specified folder location. 

Navigate using cd within command prompt to GitHub repository location.

Type py -m pip install --upgrade pip 

Type py -m pip install --user virtualenv

Type py -m venv env

Type .\env\Scripts\activate

These commands upgrade pip and install a virtual environment to use for your python library package installs.

To get all the library packages installed, type pip install -r requirements.txt

Test that programs run correctly.
