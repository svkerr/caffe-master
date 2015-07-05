
# coding: utf-8

# Classifying ImageNet: the instant Caffe way
# ===========================================
# 
# Caffe provides a general Python interface for models with `caffe.Net` in `python/caffe/pycaffe.py`, but to make off-the-shelf classification easy we provide a `caffe.Classifier` class and `classify.py` script. Both Python and MATLAB wrappers are provided. However, the Python wrapper has more features so we will describe it here. For MATLAB, refer to `matlab/caffe/matcaffe_demo.m`.
# 
# Before we begin, you must compile Caffe and install the python wrapper by setting your `PYTHONPATH`. If you haven't yet done so, please refer to the [installation instructions](installation.html). This example uses our pre-trained CaffeNet model, an ILSVRC12 image classifier. You can download it by running `./scripts/download_model_binary.py models/bvlc_reference_caffenet`. Note that this pre-trained model is licensed for academic research / non-commercial use only.
# 
# Ready? Let's start.

# In[2]:

import pdb

caffe_root='/home/stuart/caffe-master/'   # redefining caffe-root (vice line below) 
# caffe_root = '../'  # this file is expected to be in {caffe_root}/examples

import sys
import os

cf=caffe_root+'python'
os.walk(cf)
sys.path.insert(0, cf)
import numpy as np
import matplotlib.pyplot as plt

import caffe

MODEL_FILE = '/home/stuart/caffe-master/examples/cifar10/basics/cifar10_quick.prototxt'
PRETRAINED = '/home/stuart/caffe-master/examples/cifar10/basics/cifar10_quick_iter_1000.caffemodel'
mean_file ="/home/stuart/caffe-master/examples/cifar10/basics/mean_test.npy"
mean = np.load(mean_file)

net= caffe.Classifier(MODEL_FILE, PRETRAINED,
		mean=mean,
		raw_scale=255,
		image_dims=(64, 64))

for f in open("/tmp/testing_images/car_testing.dat"):
	IMAGE_FILE,LABEL = (f.split(" "))
	input_image = caffe.io.load_image(IMAGE_FILE,color=False)
	##
	net.set_phase_test()
	net.set_mode_cpu()
	#
	pdb.set_trace()
	input_image = caffe.io.load_image(IMAGE_FILE,color=False)
	prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
	#prediction = net.predict([input_image], oversample=False)
	print IMAGE_FILE+","+str(np.argmax(prediction))+","+LABEL.strip()
