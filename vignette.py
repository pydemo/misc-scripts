#!/usr/bin/python

'''
This example illustrates how to use Hough Transform to find lines

Usage:
    houghlines.py [<image_name>]
    image argument defaults to ../data/pic1.png
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math
from numpy import zeros, uint8
from datetime import  datetime
from sys import exit
import os
from types import *

e=exit
ts = str(datetime.utcnow()).replace(' ','_').replace(':','_')
print (ts)
#e(0)
# read image
models='SAMSUNG_100MSDCF' 
models=r'insta\ukraine' 
models='lino22'
in_path='in/%s' % models
#in_path=r'C:\Users\a lex_buz\Pictures\Samsung\100MSDCF'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:

        
if __name__ == '__main__':

    print(__doc__)

    import cv2
    import numpy as np


    out_path=os.path.join(in_path,'vignette_'+models,ts)

    if not os.path.isdir(out_path): 
        os.makedirs(out_path)   
    #e(0)
    for i,f in enumerate(os.listdir(in_path)):
        in_img=os.path.join(in_path,f)
        print (f)
        if os.path.isdir(in_img):
            continue
        out_img=os.path.join(out_path,f)        
        #img = cv2.imread(in_img)
        img = cv2.imread(in_img)
        rows, cols = img.shape[:2]

        kernel_x = cv2.getGaussianKernel(cols,200)
        kernel_y = cv2.getGaussianKernel(rows,200)
        kernel = kernel_y * kernel_x.T
        mask = 255 * kernel / np.linalg.norm(kernel)
        output = np.copy(img)

        # applying the mask to each channel in the input image
        for i in range(3):
            output[:,:,i] = output[:,:,i] * mask

        #cv2.imshow('Original', img)
        #cv2.imshow('Vignette', output)
        #cv2.waitKey(0)
        #e(0)
        #cv2.imshow('Input', img)
        #cv2.imshow('Erosion', img_erosion)
        #cv2.imshow('Dilation', img_dilation)

        #cv2.waitKey(0) 
        #e(0)           
        cv2.imwrite(os.path.join(out_path, "vignette_%s" %  f), output)
        #cv2.imwrite(os.path.join(out_path, "dilation_%s" %  f), img_dilation)
        #cv2.imwrite(os.path.join(out_path, "emboss_nw_%s" %  f), output_3)


