import os
import numpy as np
import matplotlib.pyplot as plt
from numpy import asarray
from numpy import save

import nibabel as nib


import csv

filename = 'ADNI.csv'
with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in readCSV:
        i = i+1
        if i != 1:
            path = row[6]
            path1 = path+"mri/brain.mgz"

            try:
                img = nib.load(path1)
                data = img.get_fdata()
                data = data[:,:,:]
                npy_convert = asarray(data)
                print((npy_convert.shape))

                # save to npy file
                save(row[1]+'.npy', npy_convert)

            except FileNotFoundError:
                print(row[5], "_lh.curv File Not Found")

