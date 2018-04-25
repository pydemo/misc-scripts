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
models='lino24'
in_path='in/%s' % models
#in_path=r'C:\Users\a lex_buz\Pictures\Samsung\100MSDCF'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:
from PIL import Image
        
if __name__ == '__main__':

    print(__doc__)


    #gscale_name='IMREAD_GRAYSCALE'

    out_path=os.path.join('out',models,'crop_blend',ts)

    if not os.path.isdir(out_path): 
        os.makedirs(out_path)   
    #e(0)
    blend_in=None
    for i,f in enumerate(os.listdir(in_path)):
        in_img=os.path.join(in_path,f)
        print (f)
        if os.path.isdir(in_img):
            continue
        if not blend_in:
            blend_in_bn=f
            blend_in=in_img

        out_img=os.path.join(out_path,blend_in_bn+'.'+f)        
        #fn = "../data/pic1.png"

         
        #import Image

        #img = Image.open(in_img)
        #img_1 = cv2.imread(in_img)
        img1 = Image.open(in_img)
        img1 = img1.convert('RGBA')
        #height1, width1, channels = img_1.shape
        (width1,height1)=img1.size
        print (height1, width1)
        #e(0)
        #img_2 = cv2.imread(blend_in)
        img2 = Image.open(blend_in)
        img2 = img2.convert('RGBA')
        #height2, width2, channels = img_2.shape
        (width2,height2)=img2.size
        print (height2, width2)
        #img1.show()
        #print(img1.size)
        if height1>height2:
            print('resize', ( width2,height2))
            area = (0, 0, width2, height2)
            img1 = img1.crop(area)
            print(img1.size)
        else:
            print('resize2', ( width2,height2))
            area = (0, 0, width1, height1)
            img2 = img2.crop(area)
            print(img2.size)           
        #img = Image.blend(img1, img2, 0.6)
        #background = Image.open("test1.png")
        #foreground = Image.open("test2.png")

        #img2.paste(img1, (0, 0), img1)
        img3=Image.alpha_composite(img1, img2)
        #https://stackoverflow.com/questions/5324647/how-to-merge-a-transparent-png-image-with-another-image-using-pil
        img3.show()

        #img.show()
        cv2.waitKey()
        img2.save(out_img)
        #img.show()
        #img2.show()
        #cv2.waitKey(1)
        #cv2.imwrite(out_img, im)
        #cv2.imshow("color swap", im)
        #cv2.waitKey(0)
        #cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)

        #cv2.imwrite('imageAdded.png', output)


        #cv2.imshow("detected lines", square)
        #cv2.waitKey(0)

        #e(0)
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
