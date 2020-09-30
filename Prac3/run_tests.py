import os, subprocess  # to navigade folders and call scripts, makefile, etc
from itertools import product  # to find all possible combinations between flags, bit-witdhs and threads

from write_line_to_file import write_line_to_file

flags = list(product(['-O0', '-O1', '-O2', '-Ofast', '-Os', '-Og'], ['', '-funroll-loops']))
bit_widths = ['double', 'float', '__fp16']

os.chdir('C')
type = ''

for combo in flags:
    flag = "-lm -lrt " + ' '.join(combo)
    for bit_width in bit_widths:
        if bit_width != '__fp16':
            flag += ' ' + "-mfp16-format=ieee"
            type = 'float'
        elif bit_width == 'float':
            type = 'float'
        else:
            type = 'double'
        
        for file in ["C/CHeterodyning.c", "C/CHeterodyning_threaded.c", "C/globals.h"]:
            with open(file, "r+") as f:
                code = f.read()
                if type == 'float':
                    code = code.replace("double carrier", f"{type} carrier")
                    code = code.replace("double data", f"{type} data")
                    code = code.replace("double result", f"{type} result")
                else:
                    code = code.replace("float carrier", f"{type} carrier")
                    code = code.replace("float data", f"{type} data")
                    code = code.replace("float result", f"{type} result")
              
        write_line_to_file("makefile", keywords=['CFLAGS'], line_to_add=f"CFLAGS = {flag}\n")  # repurposing the function

        subprocess.run(['make'])
        subprocess.run(['make', 'run_many'])
        # subprocess.run(['make', 'threaded'])
        # subprocess.run(['make', 'run_threaded_many'])
