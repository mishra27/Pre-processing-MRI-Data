import nibabel as nib
import numpy as np
import csv


with open('file.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        data = np.load(row[0])
        img = nib.Nifti1Image(data, np.eye(4)) 
        img.to_filename((row[0][:-4]+'.nii.gz'))	
           
