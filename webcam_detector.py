
#import everything
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

#make argrument parser to handle the arguments from commandprompt, but we don't need it
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

#get webcam as source 0 and make a videostream
vs = VideoStream(src=0).start()
vs2 = VideoStream(src=1).start()
time.sleep(2.0)
while True:
	#Scroll through the frames every loop
	frame = vs.read()
	frame2 = vs2.read()
	#if there is no frame, something went wrong or webcam is disabled or something
	if frame is None or frame2 is None:
		print("Noppes")
		break
	
 	#idk, the video is shown
	frame = imutils.resize(frame, width=500)
	frame2 = imutils.resize(frame2, width=500)
	cv2.imshow("Security Feed", frame)	
	cv2.imshow("Security Feed 2", frame2)	
	# if the `q` key is pressed, break from the loop
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
 