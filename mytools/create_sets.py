# parses a directory of images into training and test sets, and places them into respective test and training directories
# NOTES:
# 1. Executed in directory at same level of directory where image set to be parsed is contained

import pdb
import shutil
import os
import glob

fnames = glob.glob('./Car_Positives/*.jpg')	# glob (vs listdir) allows specifiying only *.jpg

indices = range(len(fnames))

pdb.set_trace()

testList = [fnames[i] for i in indices if i%3 == 0]		# test list is 30% of total
trainList = [fnames[i] for i in indices if i%3 !=0]		# train list is 70% of total


files = glob.glob('/home/stuart/Pictures/testSet/*')		# remove current testing files
for f in files:
	os.remove(f)

files = glob.glob('/home/stuart/Pictures/trainSet/*')		# remove current training files
for f in files:
	os.remove(f)

for name in testList:						# populate testing file directory
	shutil.copy(name, './testSet/')
for name in trainList:						# populate training file directory
	shutil.copy(name, './trainSet/')

