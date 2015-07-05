#!/bin/bash
ROOT=/home/stuart/caffe-master

# Remove previous leveldb files:
rm -r $ROOT/examples/cifar10/basics/car10_train_leveldb
rm -r $ROOT/examples/cifar10/basics/car10_test_leveldb

$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb -gray=true $ROOT/make_car/car_image_dataset/training_images/ $ROOT/make_car/car_training.dat  $ROOT/examples/cifar10/basics/car10_train_leveldb
 
$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb -gray=true $ROOT/make_car/car_image_dataset/testing_images/ $ROOT/make_car/car_testing.dat $ROOT/examples/cifar10/basics/car10_test_leveldb  

