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

# Main function
def main(last_time=False):  # when calling main for the last time, last_time will be True
    # print("There are {} samples".format(len(c)))
    # print("using type {}".format(type(data[0])))
    Timing.startlog()
    for i in range(len(c)):
        result.append(c[i] * d[i])
    Timing.endlog(last_time)

# Only run the functions if this module is run
if __name__ == "__main__":
    import time
    
    try:
        with open("sheet.csv", "r+") as sheet:
            lines = sheet.readlines()
            # print(lines)
            # looking for the "Python" line to overwrite it
            for i in range(len(lines)):
                if lines[i].startswith("Python,"):  # if the file contains a line for Python, 
                    # print("found line:", lines[i])
                    lines[i] = "Python,\n"
                    # lines.pop(i)  # delete that line
                    break
            
            else:  # if there was no line starting with "Python," (the loop didn't break)
                lines.append("Python,")

            sheet.seek(0)
            sheet.truncate()  # clearing the file and rewriting the contents
            # lines.append("Python,")  # create a new line for Python at the end of the file
            sheet.writelines(lines)  # rewrite the file.
            lines = sheet.readlines()
            

            

    except FileNotFoundError:
        with open("sheet.csv", "w+") as sheet:
            sheet.write("Python,\n")

    try:
        # time.sleep(1)
        # run main 20 times, so that the execution times will be logged in a csv file
        for i in range(2):
            # time.sleep(0.25)
            main()
        # calling main one last time
        main(last_time=True)

        # adding a newline to the end of the file
        with open("sheet.csv", "a") as sheet:
            sheet.write("\n")

    except KeyboardInterrupt:
        print("Exiting gracefully")

    except Exception as e:
        print("Error: {}".format(e))
