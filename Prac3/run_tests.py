import os, subprocess  # to navigade folders and call scripts, makefile, etc
from itertools import product  # to find all possible combinations between flags, bit-witdhs and threads

from write_line_to_file import write_line_to_file

flags = list(product(['-O0', '-O1', '-O2', '-Ofast', '-Os', '-Og'], ['', '-funroll-loops']))
bit_widths = ['double', 'float', '__fp16']

os.chdir('C')

for combo in flags:
    flag = "-lm -lrt " + ' '.join(combo)
    print(flag)
    write_line_to_file("makefile", keywords=['CFLAGS'], line_to_add=f"CFLAGS = {flag}\n")  # repurposing the function

    subprocess.run(['make'])
    subprocess.run(['make', 'run_many'])



# subprocess.run(['make', 'run_many'])
# subprocess.run(['clear'])
# subprocess.

