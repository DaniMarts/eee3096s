import os, subprocess  # to navigade folders and call scripts, makefile, etc
from itertools import product  # to find all possible combinations between flags, bit-witdhs and threads

from write_line_to_file import write_line_to_file

def main():
    c_flags = list(product(['-O0', '-O1', '-O2', '-O3', '-Ofast', '-Os', '-Og'], ['', '-funroll-loops']))  # combining the -O flags with -funroll-loop or nothing
    bit_widths = ['double', 'float', '__fp16']
    thread_counts = [2, 4, 8, 16, 32]


    # testing the python script
    subprocess.run(["python3", "Python/PythonHeterodyning.py"])

    os.chdir('C')
    type = ''

    # iterating over the flags
    for combo in c_flags:
        flag = "-lm -lrt " + ' '.join(combo)

        # iterating over the bit-widths
        for bit_width in bit_widths:
            if bit_width == '__fp16':
                flag += ' ' + "-mfp16-format=ieee"  # adding the flag only for __fp16. float and double don't need it
            
            # chaning the compiler flags in the makefile
            write_line_to_file("makefile", keywords=['CFLAGS'], line_to_add=f"CFLAGS = {flag}\n")  # repurposing the function

            # changing the data types (bit-widths) in the C files
            write_line_to_file("src/globals.h", keywords=['TYPE'], line_to_add=f"#define TYPE {bit_width}\n") 

            # changing the bit-width in the makefile, for annotation purposes only
            write_line_to_file("makefile", keywords=['BIT_WIDTH'], line_to_add=f"BIT_WIDTH = {bit_width}\n")

            # calling make with the current flags, for unthreaded, and then running it
            subprocess.run(['make'])
            subprocess.run(['make', 'run_many'])

            # iterating over the thread-counts
            for threads in thread_counts:
                write_line_to_file("src/CHeterodyning_threaded.h", keywords=['Thread_Count'], line_to_add=f"#define Thread_Count {threads}\n") 
                # changing the thread-count in the makefile, for annotation purposes only
                write_line_to_file("makefile", keywords=['THREAD_COUNT'], line_to_add=f"THREAD_COUNT = {threads}\n")
                
                # calling make with the current flags, for threaded, and then running it
                subprocess.run(['make', 'threaded'])
                subprocess.run(['make', 'run_threaded_many'])

# Only run the functions if this module is run
if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("Exiting gracefully")

    except Exception as e:
        print("Error: {}".format(e))
