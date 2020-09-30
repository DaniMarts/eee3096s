import os, subprocess  # to navigade folders and call scripts, makefile, etc
from itertools import product  # to find all possible combinations between flags, bit-witdhs and threads

flags = list(product(['-O0', '-O1', '-O2', '-Ofast', '-Os', '-Og'], ['', '-funroll-loops']))

with open("C/makefile", "r+"):
    pass
print(len(flags))
# os.chdir('C')

# subprocess.run(['make', 'run_many'])
# subprocess.run(['clear'])
# subprocess.

