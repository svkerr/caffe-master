# import the necessary packages
import sliding_window
import argparse
import time
import cv2
import cv 
import pdb 
import numpy as np 
import classifier
import skimage
###
pdb.set_trace()
net = classifier.classifier() 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image and define the window width and height
image = cv2.imread(args["image"],cv2.CV_LOAD_IMAGE_GRAYSCALE)
(winW, winH) = (64,64)
for (x,y,window) in sliding_window.sliding_window(image,stepSize = 8, windowSize=(winW, winH)):
	if window.shape[0] != winH or window.shape[1] != winW:
		continue
	window = window[:, :, np.newaxis]
	w = skimage.img_as_float(window).astype(np.float32)
	prediction = net.predict([w])
	print x,y,prediction[0][1]
	cv2.imshow("Window",window)	
	clone = image.copy()
	if prediction[0][1] >.4:
		cv2.circle(image,(x+32,y+32),4,(255,255,0),-1)	
	cv2.rectangle(clone,(x,y),(x+winW,y+winH),(255,255,0),2)
	cv2.imshow("Window", clone)
	cv2.waitKey(1)
	time.sleep(.005) 		
