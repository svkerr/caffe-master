#!/bin/bash
for f in *.jpg; do
filename=$(basename $f);
extension="${filename##*.}";
filename="${filename%.*}";
outFile=./gray/$filename"_gray.jpg"
echo $outFile
convert -colorspace Gray $f $outFile;
done;
