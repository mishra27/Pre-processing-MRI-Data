# Cortical Thickness Graph Creation for GCNs

- The first step is to Resample <freesurfer_output_subject>/surf/lh.thickness onto fsaverage. Official doc [here](https://surfer.nmr.mgh.harvard.edu/fswiki/mris_preproc)
  - Setup Freesurfer environments and update the SUBJECTS_DIR that contains processed subject directories.
  - In the ``SUBJECTS_DIR`` copy the fsaverage directory located in Freesurfer folder ```/freesurfer/subjects/fsaverage```.
  - ```mris_preproc --s $f \ --target fsaverage --hemi rh --meas thickness --out rh.thickness.mgh``` This maps the right hemisphere cortical thickness of subject $f onto fsaverage subject's rh and save in rh.thickness.mgh. Run ```mris_preproc.sh``` script in subject directory to process all the subjects.

Now each of the subject has been resampled to fsaverage brain with 163842 vertices. To read the ```rh.thickness.mgh``` an example is shown in ```read_mgh.py``` file. The output of this will return a list of lists where the first index is the cortical thickness of the vertex 1 and so on. Therefore the size of the retured list is 163842 X 1
