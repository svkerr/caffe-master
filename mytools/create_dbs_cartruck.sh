#!/bin/bash
ROOT=/home/stuart/caffe-master

# Remove previous leveldb files:
rm -r $ROOT/examples/cifar10/basics/car_truck_train_leveldb
rm -r $ROOT/examples/cifar10/basics/car_truck_test_leveldb

$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb -gray=true $ROOT/make_car_truck/car_truck_dataset/training_images/ $ROOT/make_car_truck/car_truck_dataset/car_truck_training.dat  $ROOT/examples/cifar10/basics/car_truck_train_leveldb
 
$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb -gray=true $ROOT/make_car_truck/car_truck_dataset/testing_images/ $ROOT/make_car_truck/car_truck_dataset/car_truck_testing.dat $ROOT/examples/cifar10/basics/car_truck_test_leveldb  

