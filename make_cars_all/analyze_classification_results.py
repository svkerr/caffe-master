
import sys
import os
hit = 0.0
miss = 0.0
fp = 0.0
fn = 0.0
tp = 0.0

file = open("results_class")
for line in file:
	FILENAME,PRED,ACTUAL = (line.strip()).split(",")
        if PRED == ACTUAL:
		hit = hit + 1
        else:
		miss = miss + 1

	if PRED == str(1) and ACTUAL == str(0):
		fp = fp + 1
	if PRED == str(0) and ACTUAL == str(1):
		fn = fn + 1
	if PRED == str(1) and ACTUAL == str(1):
		tp = tp + 1

accuracy = hit/(hit + miss)
precision =  tp / (tp + fp)
print "\nhit = "+str(hit)
print "miss = "+str(miss)
print "false positives = "+str(fp)
print "false negatives = "+str(fn)
print "accuracy = "+str(accuracy)
print "precision = "+str(precision)
