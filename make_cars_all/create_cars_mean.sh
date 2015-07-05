#!/bin/bash
ROOT=/home/stuart/caffe-master
DBTYPE=leveldb

# This script calculates mean of pools train and test leveldb files

# Remove previous mean binaryproto files:
rm -r $ROOT/make_cars_all/mean_train_cars_all.binaryproto
rm -r $ROOT/make_cars_all/mean_test_cars_all.binaryproto

echo "Creating mean..." 
$ROOT/build/tools/compute_image_mean.bin -backend=$DBTYPE $ROOT/make_cars_all/cars_all_train_$DBTYPE $ROOT/make_cars_all/mean_train_cars_all.binaryproto  
$ROOT/build/tools/compute_image_mean.bin -backend=$DBTYPE $ROOT/make_cars_all/cars_all_test_$DBTYPE $ROOT/make_cars_all/mean_test_cars_all.binaryproto 

echo "Done." 
