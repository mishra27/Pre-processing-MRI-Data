# Cortical Thickness Graph Creation for GCNs

- The first step is to Resample <freesurfer_output_subject>/surf/lh.thickness onto fsaverage. Official doc [here](https://surfer.nmr.mgh.harvard.edu/fswiki/mris_preproc)
  - Setup Freesurfer environments and update the SUBJECTS_DIR that contains processed subject directories.
  - In the ``SUBJECTS_DIR`` copy the fsaverage directory located in Freesurfer folder ```/freesurfer/subjects/fsaverage```.
  - ```mris_preproc --s $f \ --target fsaverage --hemi rh --meas thickness --out rh.thickness.mgh``` This maps the right hemisphere cortical thickness of subject $f onto fsaverage subject's rh and save in rh.thickness.mgh. Run ```mris_preproc.sh``` script in subject directory to process all the subjects.

Now each of the subject has been resampled to fsaverage brain with 163842 vertices. To read the ```rh.thickness.mgh``` an example is shown in ```read_mgh.py``` file. The output of this will return a list of lists where the first index is the cortical thickness of the vertex 1 and so on. Therefore the size of the retured list is 163842 X 1

Now you can create an adjacency matrix using the rh.pial surface from fsaverage, since all the subjects are mapped to it. The returned matrix will be of size 163842 X 163842. You can use Won Hwa Kim's [CTA_toolbox](http://ranger.uta.edu/~wonhwa/cta_toolbox.html) to read the sruface and create the adjacency matrix. Once you have the tool box downloaded and added to the path you can run main.m to get the vertices faces and Graph laplacial adjacency matrix. You can now use the cortical thickness files of shape 163842 X n, where n is number of subjects, and 163842 X 163842 adjacency matrix to run a GCN algorithm. An example of spectral GCN on cortical thickness is given [here](https://github.com/bieqa/LB-CNN) 

