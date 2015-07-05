# labels2.py
# append a <space> and flag onto file name depending whether it is a target (1) or not (0)
# redirect output to car_testing.dat (for example)
# NOTE: differs from labels.py in that this uses glob package

import numpy as np
from glob import glob

files = glob('*.jpg')

for f in files:
	flag = 0 
        if 'pos' in f:
        	flag =1
		print f,flag
	else:
		print f,flag

