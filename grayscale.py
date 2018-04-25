import cv2, os, sys
e=sys.exit

#cv2.imshow('Grayscale', gray_img)
#cv2.waitKey()
in_path='in/models'
gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
for gscale_name in gsnl:
	#gscale_name='IMREAD_GRAYSCALE'
	out_path=os.path.join('out','models',gscale_name)
	if not os.path.isdir(out_path): 
		os.mkdir(out_path)

	gs=eval('cv2.%s' % gscale_name)
	print gs, gscale_name
	#e(0)
	for i,f in enumerate(os.listdir(in_path)):
		#print i,f
		gray_img=cv2.imread(os.path.join(in_path,f),gs)
		cv2.imwrite(os.path.join(out_path,f), gray_img)

