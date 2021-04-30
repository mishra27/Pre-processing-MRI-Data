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

        for f,i in zip(fnames, range(0,len(fnames))):
	 
            tmp = np.load(self.datapath+f+".npy")
            
            print(i, "  ", f+".npy " )

            val = input("rotate anti-clock x time") 

            if val == "w":
                np.save(f+"_rotated"+'.npy', tmp) 
                plt.close('all')

            while( val != "w" ):
               
                val = int(val)
                for i in range(256):

                    tmp[i] = np.rot90(tmp[i], val)
                    tmp[i] = np.rot90(tmp[i], val)
                    tmp[i] = np.rot90(tmp[i], val)
                
                val = input("y to save or num to rotate") 

                if val == "w":
                   np.save(f+"_rotated"+'.npy', tmp) 
	   
                  
        return 

Rotate(1,0.5)
