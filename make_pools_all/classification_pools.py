
# coding: utf-8

# Caffe provides a general Python interface for models with `caffe.Net` in `python/caffe/pycaffe.py`, but to make off-the-shelf classification easy we provide a `caffe.Classifier` class and `classify.py` script. Both Python and MATLAB wrappers are provided. However, the Python wrapper has more features so we will describe it here. For MATLAB, refer to `matlab/caffe/matcaffe_demo.m`.
# 
# Before we begin, you must compile Caffe and install the python wrapper by setting your `PYTHONPATH`. If you haven't yet done so, please refer to the [installation instructions](installation.html). This example uses our pre-trained CaffeNet model, an ILSVRC12 image classifier. You can download it by running `./scripts/download_model_binary.py models/bvlc_reference_caffenet`. Note that this pre-trained model is licensed for academic research / non-commercial use only.
# Note: In my .bashrc file I added: export PYTHONPATH="${PYTHONPATH}:/home/stuart/caffe-master/python" 

import pdb
import numpy as np
import matplotlib.pyplot as plt
import caffe

MODEL_FILE = '/home/stuart/caffe-master/make_pools_all/pools_quick.prototxt'
PRETRAINED = '/home/stuart/caffe-master/make_pools_all/pools_quick_iter_2000.caffemodel'
mean_file ='/home/stuart/caffe-master/make_pools_all/out.npy'

mean = np.load(mean_file)

net= caffe.Classifier(MODEL_FILE, PRETRAINED,
		mean=mean,
		channel_swap=(2,1,0),
		raw_scale=255,
		image_dims=(64, 64))  # added first dimension (color) versus previous gray-scale images

for filename in open("/home/stuart/Pictures/PoolsAll/testSet/pools_all_testing.dat"):
	IMAGE_FILE,LABEL = (filename.split(" "))
#	pdb.set_trace()
	input_image = caffe.io.load_image(IMAGE_FILE, color=True)
	prediction = net.predict([input_image], oversample=False)
	print IMAGE_FILE+","+str(np.argmax(prediction))+","+LABEL.strip()

