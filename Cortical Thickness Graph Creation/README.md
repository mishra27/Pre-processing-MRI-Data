# Cortical Thickness Graph Creation for GCNs

- The first step is to Resample <freesurfer_output_subject>/surf/lh.thickness onto fsaverage
  - Setup Freesurfer environments and update the SUBJECTS_DIR that contains processed subject directories.
  - In the ``SUBJECTS_DIR`` copy the fsaverage directory located in Freesurfer folder ```/freesurfer/subjects/fsaverage```.
  - ```mris_preproc --s $f \ --target fsaverage --hemi rh --meas thickness --out rh.thickness.mgh``` This maps the right hemisphere cortical thickness of subject $f onto fsaverage subject's rh and save in rh.thickness.mgh. Run ```mris_preproc.sh``` script in subject directory to process all the subjects.
