#!/usr/bin/env sh

ROOT=/home/stuart/caffe-master
TOOLS=$ROOT/build/tools

$TOOLS/caffe train \
  --solver=$ROOT/examples/cifar10/basics/cifar10_quick_solver.prototxt

 reduce learning rate by factor of 10 after 8 epochs
#$TOOLS/caffe train \
#  --solver=$ROOT/examples/cifar10/cifar10_quick_solver_lr1.prototxt \
#  --snapshot=$ROOT/examples/cifar10/cifar10_quick_iter_4000.solverstate
