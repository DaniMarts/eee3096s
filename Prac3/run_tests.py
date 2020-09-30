import os, subprocess  # to navigade folders and call scripts, makefile, etc
from itertools import product  # to find all possible combinations between flags, bit-witdhs and threads

from write_line_to_file import write_line_to_file

c_flags = list(product(['-O0', '-O1', '-O2', '-Ofast', '-Os', '-Og'], ['', '-funroll-loops']))  # combining the -O flags with -funroll-loop or nothing
bit_widths = ['double', 'float', '__fp16']
thread_counts = [1, 2, 4, 8, 16, 32]

os.chdir('C')
type = ''

# iterating over the flags
for combo in c_flags:
    flag = "-lm -lrt " + ' '.join(combo)

    # iterating over the bit-widths
    for bit_width in bit_widths:
        if bit_width == '__fp16':
            # flag += ' ' + "-mfp16-format=ieee"
            type = 'float'
        else:
            type = bit_width
        
        # chaning the compiler flags in the makefile
        # write_line_to_file("makefile", keywords=['CFLAGS'], line_to_add=f"CFLAGS = {flag}\n")  # repurposing the function

        #region changing the data types (bit-widths) in the C files
        write_line_to_file("src/globals.h", keywords=['TYPE'], line_to_add=f"#define TYPE {type}\n") 

        # with open("src/globals.h", "r+") as f:  # this is the only file that needs to be modified, as the datatype only depends on TYPE, which is defined there
        #     lines = f.readlines()
        #     for num in range(len(lines)):
        #         if "define TYPE" in (lines[num]):
        #             lines[num] = f"#define TYPE {type}\n"
        #             break
            
        #     # rewriting the file
        #     f.seek(0)
        #     f.truncate()
        #     f.writelines(lines)
        #endregion

        # changing the bit-width in the makefile, for annotation purposes only
        # write_line_to_file("makefile", keywords=['BIT_WIDTH'], line_to_add=f"BIT_WIDTH = {bit_width}\n")

        # iterating over the thread-counts
        # for threads in thread_counts:
            
        # running make with the current flags, for unthreaded, and then running it
        # subprocess.run(['make'])
        # subprocess.run(['make', 'run_many'])

        
        # running make with the current flags, for threaded, and then running it
        # subprocess.run(['make', 'threaded'])
        # subprocess.run(['make', 'run_threaded_many'])
