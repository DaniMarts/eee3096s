import sys  # just to read command line arguments
from write_line_to_file import write_line_to_csv

def main(c_flags):
    print(c_flags)
    write_line_to_csv("sheet.csv", c_flags)

if __name__ == "__main__":
    sys.argv.pop(0)
    main(sys.argv)