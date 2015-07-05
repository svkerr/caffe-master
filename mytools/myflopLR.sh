#!/bin/bash

# creates a copy of left/right flip of all images with its current directory

for f in *.jpg
do
filename=$(basename $f);
extension="${filename##*.}";
filename="${filename%.*}";
outFile="${filename}_flop.jpg"
echo $outFile
convert -flop $f $outFile;
done;
