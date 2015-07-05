#!/bin/bash
ROOT=/home/stuart/caffe-master
DATA=/home/stuart/Pictures/Pools

# Remove previous leveldb files:
rm -r $ROOT/make_pools/pools_train_leveldb
rm -r $ROOT/make_pools/pools_test_leveldb

$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb $DATA/trainSet/ $DATA/trainSet/pools_training.dat  $ROOT/make_pools/pools_train_leveldb
 
$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb $DATA/testSet/ $DATA/testSet/pools_testing.dat $ROOT/make_pools/pools_test_leveldb  

