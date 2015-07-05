#!/bin/bash

# creates a copy of a 45 deg rotation of all images with its current directory

for f in *.jpg
do
filename=$(basename $f);
extension="${filename##*.}";
filename="${filename%.*}";
outFile="${filename}_rot45.jpg"
echo $outFile
convert -rotate 90 $f $outFile;
done;
