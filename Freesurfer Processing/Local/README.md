# Setting up Local Freesurfer setup

- Dowload Freesurfer for Linux [freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz](https://surfer.nmr.mgh.harvard.edu/fswiki/rel6downloads)
- tar -xzvf freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz
- To begin using FreeSurfer, you need to open a terminal window and define and environment variable called FREESURFER_HOME which is set to the location FreeSurfer was extracted, and then source the setup script. Sourcing FreeSurfer needs to be done every time you open a new terminal window. Or, you can add the two lines below to your default setup file (.bashrc or .cshrc).
    - ```export FREESURFER_HOME=/location_of_fs/freesurfer```
    - ```source $FREESURFER_HOME/SetUpFreeSurfer.sh```

- Next setup sebject directory location that has the .nii.gz files (T1- weighted images)
    - ```export SUBJECTS_DIR=<path to subject data>```
    
### License
A license key must be obtained to make the FreeSurfer tools operational. Obtaining a license is free and comes in the form of a license.txt file. Once you obtain the license.txt key file, copy it to your FreeSurfer installation directory. This is also the location defined by the FREESURFER_HOME environment variable.
[License Registration Link](https://surfer.nmr.mgh.harvard.edu/registration.html


## Running a Freesurfer job
We will generate all of the Freesurfure outputs with the command recon-all, which only requires a T1-weighted anatomical image with good contrast between the white matter and the grey matter. Once you Download and Install Freesurfer you can run the following command

### Processing one subject
   ```recon-all -s sub-101 -i sub-mri-image.nii.gz -all``` (creates a folder called sub-101 in SUBJECTS_DIR where output will be stored)
 
   The ```-s``` option specifies the subject name, which you can set to whatever you want. The ```-i``` option points to the anatomical image that you will analyze; and the ```-all``` option will run all of the preprocessing steps on your data.
  
### Processing multiple subjects in a folder
Perform a full recon-all on a pre-existing subject folder

```recon-all -s output -all``` (creates a folder called output in SUBJECTS_DIR, which contains all the outputs of all the files)
