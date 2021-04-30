# for generating images from images

import numpy as np
from pathlib import Path
import sys
import os
import numpy as np
import pandas as pd
from random import seed, shuffle
import time

import nibabel as nib
from matplotlib import pyplot as plt



### DIMENSION OF 3D VOLUME
dX = 256
dY = 256
dZ = 256


# vectorized is return, check reshape lines for changing this
class Rotate():

    def __init__(self, batch_size, trainsplit=0.5):

        self.datapath = ''
        self.metapath = 'ADNI_MPRAGE_mr2pet_2_20_2020.csv'
        if Path(self.datapath).exists() and Path(self.metapath).exists():
            pass
        else:
            print('Paths specified do not exist.')
            sys.exit(0)

        self.batch_size = batch_size
        self.trainsplit = trainsplit

        metadata = pd.read_csv(self.metapath, sep=',')

        self.total_samples = metadata.shape[0]
        

        print('Loading all ADNI images (~400) into RAM...')
        X = self.load_X_data(metadata["Subject"].values).astype(np.float32)
        print('Done.\n')
   
    def show_slices(self, slices):
        """ Function to display row of image slices """
        fig, axes = plt.subplots(1, len(slices))
        for i, slice in enumerate(slices):
            axes[i].imshow(slice.T, cmap="gray", origin="lower")


    def load_X_data(self, fnames):

        #dat = np.empty((len(fnames), dX,dY, dZ), dtype=np.float32)

        for f,i in zip(fnames, range(0,len(fnames))):
	 
            tmp = np.load(self.datapath+f+".npy")
            
            print(i, "  ", f+".npy " )

            slice_0 = tmp[dX//2, :, :]
            slice_1 = tmp[:, dY//2, :]
            slice_2 = tmp[:, :, dZ//2]
            self.show_slices([slice_0, slice_1, slice_2])
            plt.suptitle("Center slices for image")  
            plt.show(block=False)

            val = input("rotate anti-clock x time") 

            if val == "w":
                np.save(f+"_rotated"+'.npy', tmp) 
                plt.close('all')

            while( val != "w" ):
               
                plt.close('all')
                #print(tmp.shape)
                #print(tmp[0].shape)
                #print(tmp[1].shape)
                #print(tmp[2].shape)
                
                # = tmp[0]
                #temp_dy = tmp[1]
                #temp_dz = tmp[2]
                val = int(val)
                for i in range(256):

                    tmp[i] = np.rot90(tmp[i], val)
                    tmp[i] = np.rot90(tmp[i], val)
                    tmp[i] = np.rot90(tmp[i], val)
                
                slice_0 = tmp[dX//2, :, :]
                slice_1 = tmp[:, dY//2, :]
                slice_2 = tmp[:, :, dZ//2]
                self.show_slices([slice_0, slice_1, slice_2])
                plt.suptitle("Center slices for image")  
                plt.show(block=False)
 

                val = input("y to save or num to rotate") 

                if val == "w":
                   np.save(f+"_rotated"+'.npy', tmp) 
	   
            #dat[i,:,:,:] = tmp
                  
        return 

Rotate(1,0.5)
