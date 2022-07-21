#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

# Creating a video capture object and reading from the input file
capture = cv2.VideoCapture('/home/atharva/mrt_assignment1/src/vision/scripts/sunflower.mp4')

# Check if video was opened successfully
if not(capture.isOpened()):
  print("Error in opening the video")

# Defining a CvBridge object
bridge = CvBridge()

# Defining talker function
def talker():

  publisher = rospy.Publisher('bigbuckbunny', Image, queue_size = 1)
  rospy.init_node('bigbuckbunny_Publisher', anonymous = True)
  # To go through the loop at a rate of n times per second (n - parameter input)
  rate = rospy.Rate(30)

  while not rospy.is_shutdown():
    ret, frame = capture.read()
    if not ret:
      break
    
    # Print debugging information to the terminal
    rospy.loginfo('publishing video frame')

    # Publish the image
    # .cv2_to_imgmsg(...) converts an OpenCV image to a ROS image message
    msg = bridge.cv2_to_imgmsg(frame, "bgr8")
    publisher.publish(msg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
  # Sleep just enough to maintain the desired rate
  rate.sleep()

  # To prevent ROS from exiting the node
  rospy.spin()

  if rospy.is_shutdown():
    capture.release()


if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException:
    pass


