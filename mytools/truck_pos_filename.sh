#!/bin/bash

# changes filename of all images with its current directory to contain 'truck_pos" prepended

for f in *.jpg
do
filename=$(basename $f);
extension="${filename##*.}";
filename="${filename%.*}";
outFile="truck_pos_${filename}.${extension}"
echo $outFile
mv $f $outFile;
done;
