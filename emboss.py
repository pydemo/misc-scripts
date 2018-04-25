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
models='lino19'
in_path='in/%s' % models
#in_path=r'C:\Users\a lex_buz\Pictures\Samsung\100MSDCF'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:

        
if __name__ == '__main__':

    print(__doc__)

    import cv2
    import numpy as np


    out_path=os.path.join(in_path,'emboss_'+models,ts)

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
        img_emboss_input = cv2.imread(in_img)

        # generating the kernels
        kernel_emboss_1 = np.array([[0,-1,-1],
                                    [1,0,-1],
                                    [1,1,0]])
        kernel_emboss_2 = np.array([[-1,-1,0],
                                    [-1,0,1],
                                    [0,1,1]])
        kernel_emboss_3 = np.array([[1,0,0],
                                    [0,0,0],
                                    [0,0,-1]])

        # converting the image to grayscale
        gray_img = cv2.cvtColor(img_emboss_input,cv2.COLOR_BGR2GRAY)

        # applying the kernels to the grayscale image and adding the offset
        output_1 = cv2.filter2D(gray_img, -1, kernel_emboss_1) + 128
        output_2 = cv2.filter2D(gray_img, -1, kernel_emboss_2) + 128
        output_3 = cv2.filter2D(gray_img, -1, kernel_emboss_3) + 128

        #cv2.imshow('Input', img_emboss_input)
        #cv2.imshow('Embossing - South West', output_1)
        #cv2.imshow('Embossing - South East', output_2)
        #cv2.imshow('Embossing - North West', output_3)
        #cv2.waitKey(0)
        #e(0)

        #cv2.waitKey(0)             
        cv2.imwrite(os.path.join(out_path, "emboss_sw_%s" %  f), output_1)
        cv2.imwrite(os.path.join(out_path, "emboss_se_%s" %  f), output_2)
        cv2.imwrite(os.path.join(out_path, "emboss_nw_%s" %  f), output_3)


