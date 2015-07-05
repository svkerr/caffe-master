#!/bin/bash
ROOT=/home/stuart/caffe-master
DATA=/home/stuart/Pictures/PoolsAll

# Remove previous leveldb files:
rm -r $ROOT/make_pools_all/pools_all_train_leveldb
rm -r $ROOT/make_pools_all/pools_all_test_leveldb

$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb $DATA/trainSet/ $DATA/trainSet/pools_all_training.dat  $ROOT/make_pools_all/pools_all_train_leveldb
 
$ROOT/.build_release/tools/convert_imageset.bin  -backend=leveldb $DATA/testSet/ $DATA/testSet/pools_all_testing.dat $ROOT/make_pools_all/pools_all_test_leveldb  

