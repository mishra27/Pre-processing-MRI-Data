# Fetching data from the FreeSurfer processed output

This script will generate text/ascii tables of freesurfer parcellation stats data (cortical stats file). More details can be found [here](https://surfer.nmr.mgh.harvard.edu/fswiki/aparcstats2table)

- parcellation stats data for right hemisphere
```aparcstats2table --subjectsfile all_subs.txt --hemi rh --parc aparc --meas thickness --tablefile adni_all_rh_thickness.txt```

- parcellation stats data for left hemisphere
```aparcstats2table --subjectsfile all_subs.txt --hemi lh --parc aparc --meas thickness --tablefile adni_all_lh_thickness.txt```

This script will generate text/ascii tables of freesurfer aseg stats data (subcortical stats file). More details can be found [here](https://surfer.nmr.mgh.harvard.edu/fswiki/asegstats2table)
```asegstats2table --subjectsfile all_subs.txt --meas volume --tablefile aseg_vol.txt```