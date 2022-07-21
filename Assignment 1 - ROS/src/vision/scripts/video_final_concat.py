#!/usr/bin/env python

# Importing the necessary libraries
import rospy
from sensor_msgs.msg import Image # Image is a message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV Library

def callback(data):

  # Used to convert between ROS and OpenCV Images
  bridge = CvBridge()

  # Receiving information about output for debugging
  rospy.loginfo("receiving video frame")

  # Convert ROS Image to message to OpenCV Image
  current_frame = bridge.imgmsg_to_cv2(data)
  current_frame_resized = cv2.resize(current_frame, (540,540))

  # Converting Image to Grayscale
  gray_image = cv2.cvtColor(current_frame_resized, cv2.COLOR_BGR2GRAY)

  # Applying gaussian low pass filter
  # gauss_image = cv2.GaussianBlur(gray_image, (3,3), sigmaX = 0, sigmaY = 0)

  # Applying canny edge detector
  edges_gray = cv2.Canny(gray_image, 50, 50)

  # Converting the gray canny edge processed image to RGB
  rgb_canny = cv2.cvtColor(edges_gray, cv2.COLOR_GRAY2RGB)

  # Convert two images into one single horizontally concatinated image
  image_hconcat = cv2.hconcat([current_frame_resized, rgb_canny])

  # Display the horizontally concatinated images
  cv2.imshow('Concatinated Video Feed', image_hconcat)
  

  cv2.waitKey(1)

def receive_message():
  
  # Tells rospy the name of the node.
  # Anonymous = true makes sure that the node has unique name
  # for ensuring th above, numbers are added to the end of the name
  rospy.init_node('bigbuckbunny_Subscriber', anonymous = True)

  # Node is subscribing to the appropriate topic (here, bigbuckbunny)
  rospy.Subscriber('bigbuckbunny', Image, callback)

  # .spin() simply keeps python from exiting this node - until the node is stopped
  rospy.spin()

  # Closes the window when stream is done
  cv2.destroyAllWindows()

if __name__ == '__main__':
  receive_message()

