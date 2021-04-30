import os
import numpy as np
import matplotlib.pyplot as plt
from numpy import asarray
from numpy import save

import nibabel as nib


import csv

with open('ADNI_MPRAGE_mr2pet_2_20_2020.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in readCSV:
        i = i+1
        if i != 1:
            path = row[1]

            #path1 = path+"mri/brain.mgz"
            #path2 = path+"surf/rh.curv.pial"

            ##print(row[5])

            try:
                img = nib.load(path+".Registered.nii")
                data = img.get_fdata()
                data = data[:,:,:]
                npy_convert = asarray(data)
                print((npy_convert.shape), " " , path)

                # save to npy file
                save(row[1]+'.npy', npy_convert)
                break

            except FileNotFoundError:
                print(row[5], "_lh.curv File Not Found")
            

"""
            try:
                img = nib.load(path2)
                data = img.get_fdata()
                data = data[:,:,:]
                npy_convert = asarray(data)
                # save to npy file
                save(row[1]+'_rh_curv_pial.npy', npy_convert)

            except FileNotFoundError:
                print(row[5], "_rh.curv File Not Found")
            else:
                print(row[5], "_rh.curv other error")
"""
