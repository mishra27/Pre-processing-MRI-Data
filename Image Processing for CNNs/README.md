# Image Processing for CNNs

### Requirements
- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation)
- [Nibabel](https://nipy.org/nibabel/installation.html)

### Steps
- Brain.mgz file from freesurfer output (located at the /mri folder of each subject output) is converted to npy file using mgz_to_npy.py script
- Use rotate_npy.py to rotate the npy files around different axis to match the templates axes.


- Use npy_to_nii.py to converty the npy files to .nii.gz file because FSL needs that format
	- Create a file called ```npy_files.csv``` containing names of all the npy files that needs to be converted, put it in the same directory as the script. 

- Finally use fsl_affine.sh script for image registration 
	- Place this script in the same folder as the .nii.gz files and run it