
import os
import matplotlib.pyplot as plt
import numpy as np
import sys
def classifier():
	caffe_root = '/home/nehal/Downloads/caffe-master/'  # this file is expected to be in {caffe_root}/examples
	cf=caffe_root+'python'
	sys.path.insert(0, cf)
	import caffe
	MODEL_FILE = '/home/nehal/Downloads/caffe-master/examples/cifar10/basics/cifar10_quick.prototxt'
	PRETRAINED = '/home/nehal/Downloads/caffe-master/examples/cifar10/basics/cifar10_quick_iter_10000.caffemodel'
	mean_file ="/home/nehal/Downloads/caffe-master/examples/cifar10/basics/mean_test.npy"
	mean = np.load(mean_file)
	net= caffe.Classifier(MODEL_FILE, PRETRAINED,
                	mean=mean,
                	raw_scale=255,
                	image_dims=(64, 64))

	
	return net

