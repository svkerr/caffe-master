#!/bin/bash
ROOT=/home/stuart/caffe-master
DBTYPE=leveldb
MYDIR=/home/stuart/caffe-master/examples/cifar10/basics

# This script calculates mean of car train and test leveldb

echo "Creating mean..." 
$ROOT/build/tools/compute_image_mean.bin -backend=$DBTYPE $MYDIR/car10_train_$DBTYPE $MYDIR/mean_train.binaryproto  
$ROOT/build/tools/compute_image_mean.bin -backend=$DBTYPE $MYDIR/car10_test_$DBTYPE $MYDIR/mean_test.binaryproto 

echo "Done." 
