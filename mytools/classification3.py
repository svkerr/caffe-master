
# coding: utf-8

# Classifying ImageNet: the instant Caffe way
# ===========================================
# 
# Caffe provides a general Python interface for models with `caffe.Net` in `python/caffe/pycaffe.py`, but to make off-the-shelf classification easy we provide a `caffe.Classifier` class and `classify.py` script. Both Python and MATLAB wrappers are provided. However, the Python wrapper has more features so we will describe it here. For MATLAB, refer to `matlab/caffe/matcaffe_demo.m`.
# 
# Before we begin, you must compile Caffe and install the python wrapper by setting your `PYTHONPATH`. If you haven't yet done so, please refer to the [installation instructions](installation.html). This example uses our pre-trained CaffeNet model, an ILSVRC12 image classifier. You can download it by running `./scripts/download_model_binary.py models/bvlc_reference_caffenet`. Note that this pre-trained model is licensed for academic research / non-commercial use only.
# 
# Ready? Let's start.


caffe_root='/home/stuart/caffe-master/'   # redefining caffe-root (vice line below) 
# caffe_root = '../'  # this file is expected to be in {caffe_root}/examples

import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

import os

import numpy as np
import matplotlib.pyplot as plt
caffe.set_mode_cpu()

MODEL_FILE = '/home/stuart/caffe-master/examples/cifar10/basics/cifar10_quick.prototxt'
PRETRAINED = '/home/stuart/caffe-master/examples/cifar10/basics/cifar10_quick_iter_1000.caffemodel'
mean_file ="/home/stuart/caffe-master/examples/cifar10/basics/mean_test.npy"
mean = np.load(mean_file)
IMAGE_FILE="/tmp/testing_images/car_pos374.jpg"
net= caffe.Classifier(MODEL_FILE, PRETRAINED,
		mean=mean,
		raw_scale=255,
		image_dims=(64, 64))

input_image=caffe.io.load_image(IMAGE_FILE)
plt.imshow(input_image)
