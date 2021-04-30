#!/bin/bash

# command to make the PATH work across operating system versions
export PATH=/bin:$PATH

# untar the freesurfer download files and change directory
tar -xzvf freesurfer.tar.gz
rm freesurfer.tar.gz
cd freesurfer

# setup freesurfer environments
export FREESURFER_HOME=`pwd`
source $FREESURFER_HOME/SetUpFreeSurfer.sh

cd ..

# set subject directory
export SUBJECTS_DIR=`pwd`

# tokenizing correct input and outout file names
fullfilename="$1"
echo "input file: $fullfilename"
filename=$(basename "$fullfilename")
fname="${filename%.*}"

# runs freesufer recon-all -all command to start processing the MRI .nii images
recon-all -sid $fname -i $fullfilename -all

# compress the output file so that it can be transfered back to submit server
tar -czvf $fname.tar.gz $fname

rm -rf freesurfer
