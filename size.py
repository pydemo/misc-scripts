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
models='lino23'
in_path='in/%s' % models
#in_path=r'C:\Users\a lex_buz\Pictures\Samsung\100MSDCF'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:

        
if __name__ == '__main__':

    print(__doc__)


    #gscale_name='IMREAD_GRAYSCALE'

    out_path=os.path.join('out',models,'houghlines',ts)

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

        img = cv2.imread(in_img)
        #get size
        height, width, channels = img.shape
        print (in_img,height, width, channels)
        # Create a black image
        x = height if height > width else width
        y = height if height > width else width
        square = np.zeros((x,y,3), np.uint8)
        square[(y-height)/2:y-(y-height)/2, (x-width)/2:x-(x-width)/2] = img
        cv2.imwrite(out_img,square)
        #cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)

        #cv2.imwrite('imageAdded.png', output)


        cv2.imshow("detected lines", square)
        cv2.waitKey(0)

        e(0)
        if 0:
            #tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
            _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
            b, g, r = cv2.split(src)
            rgba = [b,g,r, alpha]
            out = cv2.merge(rgba,4)
            cv2.imshow("detected lines", out)
            cv2.waitKey(0)
            #cv2.imwrite(out_img, out)
        #cv2.imwrite(out_img,cdst)
        #print(dir(src))
        #h1, w1 = src.height,src.width
        #h2, w2 = cdst.height,cdst.width
        #print( h1, w1,h2, w2)
        #vis = np.concatenate((src, cdst), axis=1)
        #cv2.imwrite(os.path.join(out_path, "appended_%s" %  f), vis)
        #cv2.imshow("appended_%s" % out_img, vis)
        #cv2.waitKey(0)
        #append_images(in_img, out_img)
        #e(0)
