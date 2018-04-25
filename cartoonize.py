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

def cartoonize_image(img, ds_factor=4, sketch_mode=False):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median filter to the grayscale image
    img_gray = cv2.medianBlur(img_gray, 7)

    # Detect edges in the image and threshold it
    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    # 'mask' is the sketch of the image
    if sketch_mode:
        return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Resize the image to a smaller size for faster computation
    img_small = cv2.resize(img, None, fx=1.0/ds_factor, fy=1.0/ds_factor, interpolation=cv2.INTER_AREA)
    num_repetitions = 10
    sigma_color = 5
    sigma_space = 7
    size = 5

    # Apply bilateral filter the image multiple times
    for i in range(num_repetitions):
        img_small = cv2.bilateralFilter(img_small, size, sigma_color, sigma_space)

    img_output = cv2.resize(img_small, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_LINEAR)

    dst = np.zeros(img_gray.shape)

    # Add the thick boundary lines to the image using 'AND' operator
    dst = cv2.bitwise_and(img_output, img_output, mask=mask)
    return dst

if 0:
    cap = cv2.VideoCapture(0)

    cur_char = -1
    prev_char = -1

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        c = cv2.waitKey(1)
        if c == 27:
            break

        if c > -1 and c != prev_char:
            cur_char = c
        prev_char = c

        if cur_char == ord('s'):
            cv2.imshow('Cartoonize', cartoonize_image(frame, sketch_mode=True))
        elif cur_char == ord('c'):
            cv2.imshow('Cartoonize', cartoonize_image(frame, sketch_mode=False))
        else:
            cv2.imshow('Cartoonize', frame)

    cap.release()
    cv2.destroyAllWindows()
#e(0)        
if __name__ == '__main__':

    print(__doc__)

    import cv2
    import numpy as np
    cur_char = -1
    prev_char = -1

    out_path=os.path.join(in_path,'cartoon_'+models,ts)

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
        if 1:
            frame = cv2.imread(in_img)
            #frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            c = cv2.waitKey(1)
            if c == 27:
                break

            if c > -1 and c != prev_char:
                cur_char = c
            prev_char = c
            #print(cur_char)
            #if cur_char == ord('s'):
            #cv2.imshow('Cartoonize', cartoonize_image(frame, sketch_mode=True))
            #elif cur_char == ord('c'):
            #cv2.imshow('Cartoonize', cartoonize_image(frame, sketch_mode=False))
            #else:
                #cv2.imshow('Cartoonize', frame)

            #cv2.imshow('Histogram BW', frame)
        #cv2.waitKey(0)
        #e(0)
        #img_0 = cv2.imread(in_img, 0)

        #img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        # equalize the histogram of the Y channel
        #img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

        # convert the YUV image back to RGB format
        #img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        #histeq = cv2.equalizeHist(img_0)
        #cv2.imshow('Color input image', img)
        #cv2.imshow('Histogram equalized', img_output)
        #cv2.imshow('Histogram BW', histeq)

        #cv2.waitKey(0)
        #e(0)
        #cv2.imshow('Original', img)
        #cv2.imshow('Vignette', output)
        #cv2.waitKey(0)
        #e(0)
        #cv2.imshow('Input', img)
        #cv2.imshow('Erosion', img_erosion)
        #cv2.imshow('Dilation', img_dilation)

        #cv2.waitKey(0) 
        #e(0)           
        cv2.imwrite(os.path.join(out_path, "carton_%s" %  f), cartoonize_image(frame, sketch_mode=True))
        #cv2.imwrite(os.path.join(out_path, "BW_histogram_%s" %  f), histeq)
        #cv2.imwrite(os.path.join(out_path, "dilation_%s" %  f), img_dilation)
        #cv2.imwrite(os.path.join(out_path, "emboss_nw_%s" %  f), output_3)


