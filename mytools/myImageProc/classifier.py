
import os
import matplotlib.pyplot as plt
import numpy as np
import sys
import caffe

def classifier():
	MODEL_FILE = '/home/stuart/caffe-master/make_cars_all/cars_quick.prototxt'
	PRETRAINED = '/home/stuart/caffe-master/make_cars_all/cars_quick_iter_2000.caffemodel'
	mean_file ="/home/stuart/caffe-master/make_cars_all/out.npy"
	mean = np.load(mean_file)
	net= caffe.Classifier(MODEL_FILE, PRETRAINED,
                	mean=mean,
#			channel_swap=(2,1,0),
                	raw_scale=255,
                	image_dims=(64, 64))

	
	return net

