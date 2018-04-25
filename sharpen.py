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
models='lino20'
in_path='in/%s' % models
#in_path=r'C:\Users\a lex_buz\Pictures\Samsung\100MSDCF'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:

        
if __name__ == '__main__':

    print(__doc__)

    import cv2
    import numpy as np


    out_path=os.path.join(in_path,'sharpen_'+models,ts)

    if not os.path.isdir(out_path): 
        os.makedirs(out_path)   
    #e(0)
    for i,f in enumerate(os.listdir(in_path)):
        in_img=os.path.join(in_path,f)
        print (f)
        if os.path.isdir(in_img):
            continue
        out_img=os.path.join(out_path,f)        
        img = cv2.imread(in_img)
        #cv2.imshow('Original', img)

        # generating the kernels
        kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
        kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                                     [-1,2,2,2,-1],
                                     [-1,2,8,2,-1],
                                     [-1,2,2,2,-1],
                                     [-1,-1,-1,-1,-1]]) / 8.0

        # applying different kernels to the input image
        output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
        output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
        output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

        #cv2.imshow('Sharpening', output_1)
        #cv2.imshow('Excessive Sharpening', output_2)
        #cv2.imshow('Edge Enhancement', output_3)
        #cv2.waitKey(0)
        #e(0)


        #cv2.waitKey(0)             
        cv2.imwrite(os.path.join(out_path, "sharpen_%s" %  f), output_1)
        cv2.imwrite(os.path.join(out_path, "sharpen_excessive_%s" %  f), output_2)
        cv2.imwrite(os.path.join(out_path, "sharpen_edge_enh_%s" %  f), output_3)


