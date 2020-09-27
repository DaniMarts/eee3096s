#!/usr/bin/python3
"""
Python Practical 2 Code for Timing
Keegan Crankshaw
EEE3096S Prac 2 2019
Date: 7 June 2019

Adapted from Paul McGuire's answer on Stack Overflow
https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution/12344609#12344609
"""

from time import time, strftime, localtime
from datetime import timedelta

start = ''

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def startlog():
    global start
    start = time()
    # log("Starting log")


def log(s, elapsed=None):
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)

def endlog(last_time=False):
    global start
    end = time()
    elapsed = end-start
    # log("End Program", secondsToStr(elapsed))

    # writing the elapsed microseconds to a csv file
    with open("sheet.csv", "r+") as sheet:
        # file = sheet.read()
        lines = sheet.readlines()
        # pos = file.find("Python,")

        for i in range(len(lines)):
            if lines[i].startswith("Python"):
                end_pos = sheet.read().find("Python,") + len(lines[i]) +  1
                sheet.seek(end_pos)
                break
                # if lines[i] == "Pyhton," or lines[i] == "Python,/n":  # only if there is nothing else on that line
                #     sheet.seek(pos + len("Python,"))  # move the cursor to the end of that line
                #     break  # don't go looking 
                # else:  # if that line starts with "Python," but there are other things on it, that means that line 
                #     pass
                #     lines.r

        # else:  # if there was no line starting with "Python," (the loop didn't break)
        #     lines.append("Python,")
        #     sheet.writelines(lines)  # write all the lines, with "Python,"as the last line (this is where the cursor will be)

        # Putting the cursor at the end of the corresponding line
        # pos = sheet.read().find("Python,") + len("Python,")
        # sheet.seek(pos)

        sheet.write(f"{elapsed*1000:.22f},")  # writing the time to the end of the Python line
        if last_time:
            sheet.write("\n")