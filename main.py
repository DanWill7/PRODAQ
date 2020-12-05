# Main file to run UDFs for PRODAQ the application
# Author: Daniel Williams
# Date Created: 12/5/2020 5:42PM


import ProDAQ as daq


def main():
    value = daq.test
    # references the prodaq file udf test

    print(value)


if __name__ == "__main__":
    main()
