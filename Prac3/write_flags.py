import sys  # just to read command line arguments
from write_line_to_file import write_line_to_file

def write_flags(c_flags):
    write_line_to_file("sheet.csv", c_flags)

def write_values(c_flags):
    time_values = []
    average_deviation = 0

    with open("temp.txt", "r") as temp:  # this file will be deleted by makefile after the writing operation is done
        line = temp.readline()  # the values should be on the first line
        time_values = line.split(",")
    
    with open("accuracy.txt", 'r') as accuracy:
        average_deviation = accuracy.readline()  # the value should be on the first line
    
    time_values.remove('') # since the last element after the last comma will be ''
    average_time = sum(float(value) for value in time_values)/(len(time_values)) # the average time to run the C code

    write_line_to_file("sheet.csv", c_flags, [f"{average_time:.5f}", average_deviation])
    

if __name__ == "__main__":
    if sys.argv[1] == "flags":
        write_flags(sys.argv[2:])  # the first argv is the script name, and the second is a hint for which function to run
    elif sys.argv[1] == "values":
        write_values(sys.argv[2:])