# Pre Processing T1-weighted MRI Data

## Freesurfer Processing
The first common step shared by all of the methods was that all the T1 weighted images from ADNI-2 were segmented using FreeSurfer [Fischl et al. (2002)](https://pubmed.ncbi.nlm.nih.gov/11832223/). Developed by the Laboratory for Computational Neuroimaging at the Athinoula A. Martinos Center for Biomedical Imaging, FreeSurfer is a software package that is used for analysing and visualizing neuroimaging data.

Freesurfer download and install steps can be foud [here](https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall)

### Condor
[Condor setup](Condor%20) for Freesurfer processing

### Local
We will generate all of the images mentioned above with the command recon-all, which only requires a T1-weighted anatomical image with good contrast between the white matter and the grey matter. Once you Download and Install Freesurfer you can run the following command

```ruby
recon-all -s sub-101 -i sub-101_ses-BL_T1w.nii.gz -all
```

The ```-s``` option specifies the subject name, which you can set to whatever you want. The ```-i``` option points to the anatomical image that you will analyze; and the ```-all``` option will run all of the preprocessing steps on your data.
