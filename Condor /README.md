# Condor Setup for Freesurfer processing


- Download the Freesurfer6 Linux version from [here](https://surfer.nmr.mgh.harvard.edu/fswiki/rel6downloads) and save it in submit server. 

- In the same directory put all the .nii files you want to run the freesurfer recon-all -all command. 

- Make sure you create a subject.txt file and put names of all the .nii files in there

- Put the above two .sh and sub files in the same directory as well
	- The .sub file request nodes with specific rquirements, transfers input files, retreives output files.
	- The .sh file contains the code that will run on each condor node requested

