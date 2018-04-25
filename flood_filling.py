import cv2 as cv
from numpy import zeros, uint8
from datetime import  datetime
from sys import exit
import os
e=exit
ts = str(datetime.utcnow()).replace(' ','_').replace(':','_')
print ts
#e(0)
# read image
in_path='in/models'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:

if 1:
	#gscale_name='IMREAD_GRAYSCALE'

	out_path=os.path.join('out','models',ts)

	if not os.path.isdir(out_path): 
		os.makedirs(out_path)

	
	
	#e(0)
	for i,f in enumerate(os.listdir(in_path)):
		#print i,f
		in_img=os.path.join(in_path,f)
		#cv2.imwrite(os.path.join(out_path,f), gray_img)
		out_img=os.path.join(out_path,f)
		im = cv.imread(in_img)
		h,w = im.shape[:2]

		# flood fill example
		diff = (6,6,6)
		mask = zeros((h+2,w+2),uint8)
		cv.floodFill(im,mask,(810,10), (254,254,0),diff,diff)

		# show the result in an OpenCV window
		cv.imshow('flood fill',im)
		cv.waitKey()

		# save the result
		cv.imwrite(out_img,im)
		e(0)