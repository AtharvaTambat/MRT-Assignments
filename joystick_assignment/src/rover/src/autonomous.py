#!/usr/bin/env python

from roboclaw import RoboClaw
import rospy

#---------------------------------------------------- 

class Drive:
    def __init__(self,driver1,driver2):
        self.rightClaw = driver1
        self.leftClaw = driver2
         

    def drive_callback(self,inp):
        # A bit of help! These are arrays of data
        axes = inp.axes
        buttons = inp.buttons

        if buttons[3]==1:
          self.rightClaw.ForwardM1(64)
          self.rightClaw.ForwardM2(64)
          self.leftClaw.ForwardM1(64)
          self.leftClaw.ForwardM2(64)

        elif buttons[1]==1:
          self.rightClaw.BackwardM1(64)
          self.rightClaw.BackwardM2(64)
          self.leftClaw.ForwardM1(64)
          self.leftClaw.ForwardM2(64)

        elif buttons[0]==1:
          self.rightClaw.BackwardM1(64)
          self.rightClaw.BackwardM2(64)
          self.leftClaw.BackwardM1(64)
          self.leftClaw.BackwardM2(64)

        elif buttons[2]==1:
          self.rightClaw.ForwardM1(64)
          self.rightClaw.ForwardM2(64)
          self.leftClaw.BackwardM1(64)
          self.leftClaw.BackwardM2(64)
        

    def current_limiter(self):        


        """BONUS: 

        Try to implement this function as well. It is a saftey feature. 
        How would you decide the current threshold? - Please elaborate
        """
        return False
                

#---------------------------------------------------                



