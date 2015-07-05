#!/bin/bash
ROOT=/home/stuart/caffe-master
DBTYPE=leveldb

# This script calculates mean of pools train and test leveldb files

echo "Creating mean..." 
$ROOT/build/tools/compute_image_mean.bin -backend=$DBTYPE $ROOT/make_pools_all/pools_all_train_$DBTYPE $ROOT/make_pools_all/mean_train_pools_all.binaryproto  
$ROOT/build/tools/compute_image_mean.bin -backend=$DBTYPE $ROOT/make_pools_all/pools_all_test_$DBTYPE $ROOT/make_pools_all/mean_test_pools_all.binaryproto 

echo "Done." 
