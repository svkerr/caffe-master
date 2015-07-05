#!/bin/bash

# creates a copy of top/bottom flip of all images with its current directory

for f in *.jpg
do
filename=$(basename $f);
extension="${filename##*.}";
filename="${filename%.*}";
outFile="${filename}_flip.jpg"
echo $outFile
convert -flip $f $outFile;
done;
