#!/bin/bash

# creates a copy of cropped 32x32 image of all images with its current directory

for f in *.jpg
do
filename=$(basename $f);
extension="${filename##*.}";
filename="${filename%.*}";
outFile="${filename}_crop64.jpg"
echo $outFile
convert $f -crop 64x64 +repage $outFile;
done;
