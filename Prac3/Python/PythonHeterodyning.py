#!/usr/bin/python3
"""
Python Practical Code for heterodyning and performance testing
Keegan Crankshaw
Date: 7 June 2019

This isn't necessarily performant code, but it is Pythonic
This is done to stress the differences between Python and C/C++

"""

# import Relevant Librares
import Timing
from data import carrier, data
import sys

sys.path.append("../")  # trying to import a module outside the current folder sometimes causes errors
try:  
    from Prac3.write_line_to_file import write_line_to_csv  
except ModuleNotFoundError:
    from write_line_to_file import write_line_to_csv

# Define values.
c = carrier
d = data
result = []
times = []  # a list that will be passed on to endlog(), which will append the execution times

# Main function
def main(last_time=False):  # when calling main for the last time, last_time will be True
    print("There are {} samples".format(len(c)))
    print("using type {}".format(type(data[0])))
    
    iterations = 20  # the number of times execution will be timed

    for _ in range(iterations):
        Timing.startlog()
        for i in range(len(c)):
            result.append(c[i] * d[i])
        Timing.endlog(times)

# Only run the functions if this module is run
if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("Exiting gracefully")

    except Exception as e:
        print("Error: {}".format(e))

    # after main runs, the execution times will be saved on a csv file. The times must be under the apropriate header, "Python" in this case.
    times = [*map(lambda elapsed: f"{elapsed*1e3:.22f}", times)]  # this lambda is just to format the times to 22 decimal places
    
    write_line_to_csv("sheet.csv", keywords=["Python"], values=times)
    