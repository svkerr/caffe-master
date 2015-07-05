
import sys
import os
hit = 0
miss = 0

for line in open("./car_truck_classification_results.dat"):
	FILENAME,PRED,ACTUAL = (line.split(","))
        if PRED == ACTUAL:
		hit = hit + 1
        else:
		miss = miss + 1

print "hit = "+hit
print "miss = "+miss
	
