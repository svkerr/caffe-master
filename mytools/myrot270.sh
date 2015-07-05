#!/bin/bash

# creates a copy of a 270 deg rotation of all images with its current directory

for f in *.jpg
do
filename=$(basename $f);
extension="${filename##*.}";
filename="${filename%.*}";
outFile="${filename}_rot270.jpg"
echo $outFile
convert -rotate 270 $f $outFile;
done;
