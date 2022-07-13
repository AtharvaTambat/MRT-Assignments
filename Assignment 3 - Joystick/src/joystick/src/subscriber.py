#!/usr/bin/env python
  
import rospy
from sensor_msgs.msg import Joy #importing datatype Joy
  
  
def callback(data):
      
    #rospy.loginfo("receiving data from joy topic")
    
    # Display the required message for the appropriate button pressed
    if data.buttons[3]==1:
      print("FORWARD")
    elif data.buttons[1]==1:
      print("RIGHT")
    elif data.buttons[0]==1:
      print("BACKWARD")
    elif data.buttons[2]==1:
      print("LEFT")
  
  
def main():
    
    # Naming the subscriber node
    rospy.init_node('listener', anonymous=True)

    # Subscribe to the /joy topic and to call the callback() function to print the directions
    rospy.Subscriber("joy", Joy, callback, queue_size = 1)
     
    # Prevents ROS from exiting the node
    rospy.spin()
   
  
if __name__ == '__main__':
      
    try:
        main()
    except rospy.ROSInterruptException:
        pass
