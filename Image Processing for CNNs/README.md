# Image Processing for CNNs

### Requirements
- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation)
- [Nibabel](https://nipy.org/nibabel/installation.html)

### Steps
- Brain.mgz file from freesurfer output (located at the /mri folder of each subject output) is converted to npy file using mgz_to_npy.py script
- The npy file is rotated  around different axis to match the templates axes.
- Use npy_to_nii.py to converty the npy files to .nii.gz file because FSL needs that format
- Finally use fsl_affine.sh script for image registration 