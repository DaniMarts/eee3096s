import sys  # just to read command line arguments
from write_line_to_file import write_line_to_file

def write_flags(c_flags):
    write_line_to_file("sheet.csv", c_flags)

def write_values(c_flags):
    with open("temp.txt", "r") as temp:  # this file will be deleted by makefile after the writing operation is done
        line = temp.readline()  # the values should be on the first line
        values = line.split(",")
        write_line_to_file("sheet.csv", c_flags, values)

if __name__ == "__main__":
    if sys.argv[1] == "flags":
        write_flags(sys.argv[2:])  # the first argv is the script name, and the second is a hint for which function to run
    elif sys.argv[1] == "values":
        write_values(sys.argv[2:])