# Fetching data from the FreeSurfer processed output
After setting up the Freesurfer environment and recon-all -all command, you can run the folling commands to extract stats from Freesurfers outputs to create single tables that can be used as input in different algorithms.

This script will generate text/ascii tables of freesurfer parcellation stats data (cortical stats file). More details can be found [here](https://surfer.nmr.mgh.harvard.edu/fswiki/aparcstats2table)

- parcellation stats data for right hemisphere. This will combine the rh.aparc.stats files for the subjects in all_subs.txt file to generate one table, adni_all_rh_thickness.txt, that will report the thickness of all the structures labeled in rh.aparc.annot. 
  - ```aparcstats2table --subjectsfile all_subs.txt --hemi rh --parc aparc --meas thickness --tablefile adni_all_rh_thickness.txt```

- parcellation stats data for left hemisphere. This will combine the lh.aparc.stats files for the subjects in all_subs.txt file to generate one table, adni_all_lh_thickness.txt, that will report the thickness of all the structures labeled in lh.aparc.annot. 
  - ```aparcstats2table --subjectsfile all_subs.txt --hemi lh --parc aparc --meas thickness --tablefile adni_all_lh_thickness.txt```

This script will generate text/ascii tables of freesurfer aseg stats data (subcortical stats file). More details can be found [here](https://surfer.nmr.mgh.harvard.edu/fswiki/asegstats2table)
  
-  This will combine the aseg.stats file for the subjects in all_subs.txt file to generate one table, aseg_vol.txt, that will report the volumes of all the structures labeled in aseg.mgz
    - ```asegstats2table --subjectsfile all_subs.txt --meas volume --tablefile aseg_vol.txt```
