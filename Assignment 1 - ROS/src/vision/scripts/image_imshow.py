#!/usr/bin/env python

import cv2

#read image
image = cv2.imread('/home/atharva/python_practice/lena.jpg', 1)

#display image 
cv2.imshow('lena_image', image)
cv2.waitKey(5000)

