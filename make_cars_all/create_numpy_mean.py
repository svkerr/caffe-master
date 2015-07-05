# Converts binary mean_train_pools.binaryproto file to numpy array for use in caffe Python API
# The binaryproto file is a protobuf for BlobProto. 
# Note: In my .bashrc file I added: export PYTHONPATH="${PYTHONPATH}:/home/stuart/caffe-master/python"

import os
import sys
import numpy as np

import caffe

blob = caffe.proto.caffe_pb2.BlobProto()
data = open('mean_train_cars_all.binaryproto', 'rb').read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
out = arr[0]
np.save('out.npy', out)

