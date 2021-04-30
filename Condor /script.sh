#!/bin/bash


# command to make the PATH work across operating system versions
export PATH=/bin:$PATH

# Command to enable modules, and then load an appropriate software module
#. /etc/profile.d/modules.sh
#module load freesurfer/6

# Command to run your software from the command line
#wget https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz

cp /mnt/gluster/mishra27/freesurfer.tar.gz ./

tar -xzvf freesurfer.tar.gz

#cp license.txt freesurfer

rm freesurfer.tar.gz

cd freesurfer

export FREESURFER_HOME=`pwd`
source $FREESURFER_HOME/SetUpFreeSurfer.sh

cd ..

export SUBJECTS_DIR=`pwd`

#find . -name *.nii
#fullfilename="$(echo *.nill)"
fullfilename="$1"
echo "input file: $fullfilename"
filename=$(basename "$fullfilename")
fname="${filename%.*}"
#fname="$1"


echo "fname: $fname"
echo "full: $fullfilename"
echo "file: $filename"

#recon-all -sid $fname -i $fullfilename -all
recon-all -sid $fname -i $fullfilename -all

tar -czvf $fname.tar.gz $fname

rm -rf freesurfer
