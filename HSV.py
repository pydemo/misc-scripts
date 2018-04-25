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
models='lino21'
in_path='in/%s' % models
#in_path=r'C:\Users\a lex_buz\Pictures\Samsung\100MSDCF'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:

        
if __name__ == '__main__':

    print(__doc__)


    #gscale_name='IMREAD_GRAYSCALE'

    out_path=os.path.join(in_path,'HSV_0',ts)

    if not os.path.isdir(out_path): 
        os.makedirs(out_path)   
    #e(0)
    for i,f in enumerate(os.listdir(in_path)):
        in_img=os.path.join(in_path,f)
        print (f)
        if os.path.isdir(in_img):
            continue
        out_img=os.path.join(out_path,f)        
        #fn = "../data/pic1.png"

        src = cv2.imread(in_img)
        hsv_img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        cv2.imwrite(out_img,hsv_img[:, :, 1])

        vis = np.concatenate((src, hsv_img), axis=1)
        cv2.imwrite(os.path.join(out_path, "appended_%s" %  f), vis)
