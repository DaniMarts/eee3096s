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

    #region Complicated code to write execution times to a csv file
    # after main runs, the execution times will be saved on a csv file. The times must be under the apropriate header, "Python" in this case.
    # this is what the new Python line will be
    py_line = "Python," + ','.join([*map(lambda elapsed: f"{elapsed*1e3:.22f}", times)]) + '\n'  # this lambda is just to format the times to 22 decimal places
    
    try:
        with open("sheet.csv", "r+") as sheet:  # opening the file
            lines = sheet.readlines()
            # looking for the "Python" line to overwrite it
            for i in range(len(lines)):
                if lines[i].startswith("Python,"):  # if the file contains a line for Python, 
                    lines[i] = py_line  # replace that line with the most recent execution times
                    break
            
            else:  # if there was no line starting with "Python," (the loop didn't break)
                lines.append(py_line)

            sheet.seek(0)
            sheet.truncate()  # clearing the file and rewriting the contents
            sheet.writelines(lines)  # rewrite the file.

    except FileNotFoundError: # if the file was not found, create a new one and add the execution times to it
        with open("sheet.csv", "w") as sheet:
            sheet.write(py_line)
    #endregion
    