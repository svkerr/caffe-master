
total = 0.0
count = 0.0
file = open("sliding_window_class_results")
for line in file:
	y,x,prob = (line.strip()).split(" ")
	total = total + 1
	if float(prob) > 0.70:
		count = count + 1

percent_hits = (count/total) * 100
print "total = "+str(total)
print "count = "+str(count)
print "percent hits = "+str(percent_hits)
