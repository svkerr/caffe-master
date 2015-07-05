#!/bin/bash
ROOT=/home/stuart/caffe-master
DATA=/home/stuart/Pictures/CarsAll

# Remove previous leveldb files:
rm -r $ROOT/make_cars_all/cars_all_train_leveldb
rm -r $ROOT/make_cars_all/cars_all_test_leveldb

$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb $DATA/trainSet/ $DATA/trainSet/cars_all_training.dat  $ROOT/make_cars_all/cars_all_train_leveldb
 
$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb $DATA/testSet/ $DATA/testSet/cars_all_testing.dat $ROOT/make_cars_all/cars_all_test_leveldb  

