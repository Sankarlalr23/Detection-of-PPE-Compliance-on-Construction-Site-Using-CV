import cv2
import numpy as np


max_frames = 251    #making max no. frames as 50
time_bet_frames = 5    #time in bet. frames in sec

#capturing video
vidcap = cv2.VideoCapture('videos/video10.mp4')

for i in range (1,max_frames):
    #specifying times
    time_sec = float(np.multiply(i,time_bet_frames))    #time in sec bet. frames
    time_millisec = float(np.multiply(time_sec,1000))
    vidcap.set(cv2.CAP_PROP_POS_MSEC,time_millisec)      # just cue to time_sec. position
    success,image = vidcap.read()
    if success:
        cv2.imwrite("video10frame"+str(time_sec)+"sec.jpg", image)     # save frame as JPEG file
        cv2.imshow(str(time_sec)+"sec",image)
        cv2.waitKey()
    if (i==0):
        break
