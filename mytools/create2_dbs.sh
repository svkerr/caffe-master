##!/bin/bash
ROOT=/home/stu/caffe-master
DBTYPE=lmdb

# Prepare the dataset
# This script converts car training and testing images into leveldb format
# Changed output file name from cifar10_train_leveldb to car10_train_$DBTYPE (same for test leveldb)

echo "Creating train lmdb..."
$ROOT/.build_release/tools/convert_imageset.bin  -backend=lmdb -gray=true $ROOT/make_car/car_image_dataset/training_images/ $ROOT/make_car/car_training.dat  $ROOT/examples/cifar10/basics/car10_train_$DBTYPE 


echo "Creating test lmdb..."
$ROOT/.build_release/tools/convert_imageset.bin  -backend=lmdb -gray=true $ROOT/make_car/car_image_dataset/testing_images/ $ROOT/make_car/car_testing.dat $ROOT/examples/cifar10/basics/car10_test_$DBTYPE  

echo "Done."
