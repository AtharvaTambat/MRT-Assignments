#!/usr/bin/env python

import cv2
import numpy as np


# Creating a videocapture object and read from the input file
capture = cv2.VideoCapture('/home/atharva/mrt_assignment1/src/vision/scripts/bigbuckbunny.mp4')

#Check if video was opened successfully
if(capture.isOpened()==False):
  print("Error in opening the video")

#Read until video is complete
while(capture.isOpened()):

  #Capture frame by frame
  ret, frame = capture.read()
  if ret == True:

    #Display the resulting frame
    cv2.imshow('Frame', frame)

    #Press Q on the keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  
  #Break the loop if ret != True
  else: 
    break


#When everything is done, release the video
capture.release()

#Close all frames
cv2.destroyAllWindows()

     
