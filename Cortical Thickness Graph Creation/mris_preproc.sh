#!/usr/bin/env bash
counter=0
echo "here"
for f in */ ;
do
  echo "$f"
  ((counter++))
  echo $counter
  cd "$f"
  ls
  cd surf
  mris_preproc --s $f \ --target fsaverage --hemi lh --meas thickness --out lh.thickness.mgh  
  mris_preproc --s $f \ --target fsaverage --hemi rh --meas thickness --out rh.thickness.mgh
  echo "done -$f"
  cd ..
  cd ..
done
