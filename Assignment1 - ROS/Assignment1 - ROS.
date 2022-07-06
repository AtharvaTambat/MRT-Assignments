\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}

\title{Assignment 1 - Publishing/ Subscribing an Image and Canny Edge Detection}
\author{Atharva Tambat}
\date{April 30, 2022}

\begin{document}

\maketitle

\section{Introduction}
This is the first assignment in the MRT, which consisted of 3 tasks.
\begin{enumerate}
    \item Task 1 - Make a Publisher that would publish images (instead of strings) to a rostopic using a cvbridge
    \item Task 2 - Make a subscriber for the topic and for each image use canny edge detection method to find the edges in the image and display them side by side in a single window.
    \item Task 3 - Make an rqt graph to visualize the connections between different nodes.
\end{enumerate}

\section{Task 1}
The first step while completing task 1 was to understand how to write the python script for reading a still image file and displaying the file using OpenCV. For this, the package cv2 was imported into the python script. The following are the functions used -

\begin{enumerate}
    \item cv2.imread('$<$filename$>$', $<$mode$>$) - reads the image into an object. The $<$mode$>$ can be set to 0, 1 or -1 to get a grayscale, colour and unchanged image of the original image file.
    \item cv2.imshow('$<$window heading$>$', $<$image object name$>$) - displays the image from the image object onto the window on the screen.
    \item cv2.waitKey($<$time in ms$>$) - commands the computer to show the image for the time specified in milliseconds before moving on to the next command. 
\end{enumerate}

\begin{center}
    \includegraphics[width = 0.8\textwidth]{Lena.png}
\end{center}

Next step was writing a python script for reading a video file and displaying it on the screen. For this, again, cv2 package was imported. The following functions were used (except the ones already mentioned above): 
\begin{enumerate}
    \item cv2.VideoCapture($<$Absolute path of the video file$>$) - to read the video into an object
    \item $<$videoobject$>$.isOpened() - to check whether the video file opened successfully.
    \item $<$videoobject$>$.read() - which returns values ret and frame: ret - boolean variable to check whether a frame is available and frame - a variable to store that frame.
    \item $<$videoobject$>$.release() - once everything is done, release the video.
    \item cv2.destroyAllWindows() - close all the frames at the end of the program.
\end{enumerate}

Now......ROS enters chat......
Next step was to add the extra code needed to create a publisher and publish the image to a topic, to the script that had already been written to display a video (with some slight changes).

For this some extra packages that were needed were: 
\begin{enumerate}
    \item rospy - to create a publisher and subscriber
    \item cv\textunderscore bridge - to convert the OpenCV Image to a ROS Image.
    \item sensor\textunderscore msgs.msg - to use some sensor related services and definitions (for eg: if one was using the video feed from the webcam)
\end{enumerate}

The extra methods used in this script were:
\begin{enumerate}
    \item CvBridge() - for defining  CV Bridge object.
    \item rospy.init\textunderscore node(...) - to declare this node.
    \item rospy.Publisher(...) - to declare this node as a publisher.
    \item rospy.Rate(...) - to define with what frequency should the program be run.
    \item rospy.loginfo(...) - to publish node's status to the terminal for debugging.
    \item $<$bridgeobject$>$.cv2\textunderscore to\textunderscore imgmsg(...) - to convert an OpenCV image to a ROS image message.
    \item publisher.publish(...) - to publish the message (image) to the rostopic. 
    \item rospy.sleep() - to sleep just enough to maintain the desired rate.
    \item rospy.spin() - to prevent ROS from exiting the node.
\end{enumerate}

\section {Task 2}
This task was relatively shorter than the first - because all that was left was to subscribe to the topic. A rough outline of the steps that were followed are:
\begin{enumerate}
    \item Importing necessary packages (previously mentioned packages - nothing new).
    \item Define two functions - receive\textunderscore message() and callback(data) - the former used for defining the node and declaring it as a subscriber (similar to what was done for the publisher) to the appropriate topic, and the latter used for the following:
    \begin{enumerate}
        \item Publish the status of the node for debugging.
        \item Convert ROS Image to message to OpenCV Image.
        \item Apply the canny edge method to find the edge of the images:
        \begin{enumerate}
            \item Convert the image to grayscale using cv2.cvtColor($<$name of image object$>$, cv2.COLOR\textunderscore BGR2GRAY).
            \item Apply the canny edge detection method using cv2.Canny(gray\textunderscore image, 100, 300).
            \item Convert the gray scale image to RGB to concatenate it with the original image, using cvtColor(...) function.
            \item Concatenate the images (original and th one in which edge had been detected) using cv2.hconcat(...).
            \item Display the images on the screen using cv2.imshow(...).
        \end{enumerate}
    \end{enumerate}
\end{enumerate}

\begin{center}
    \includegraphics[width = 0.8\textwidth]{sunflower_canny.png}
\end{center}


\section {Task 3}
The simplest one of the three - open new tab in the terminal and type the command: 

rosrun rqt\textunderscore graph rqt\textunderscore graph 

- Done!!!

\begin{center}
    \includegraphics[width = 0.8\textwidth]{rqt_graph_cannyedge.png}
\end{center}

NOTE: The subscriber and publisher nodes are name bigbuckbunny because I was using a 7 second clip of the big buck bunny - which proved to be too short to satisfactorily view edge detection. So, at the last moment I changed the video.

\end{document}

