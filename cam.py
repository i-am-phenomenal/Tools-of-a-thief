import cv2
from pil import  Image
import os
import time
import schedule

def getImagesCount(): 
    DIR = os.getcwd() + "/images"    
    count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) + 1
    return count

def saveImage(frame):
    imageName = "image_" + str(getImagesCount()) + ".png"
    if not cv2.imwrite(os.getcwd() + "/images/" + imageName, frame):
        raise Exception("Could not write image")

def launchWebcamAndTakeScreenshot():     
    vc = cv2.VideoCapture(0)
    vc.set(411, 1.0) # LED Selector
    vc.set(412, -2.0) # LED Mode
    vc.set(32, 0.0)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
        saveImage(frame)
        print("TOOK SCREENSHOT ")
    else:
        rval = False

    """ Removed code for opening a window """
    # while rval:
    #     rval, frame = vc.read()
    #     key = cv2.waitKey(20)
    #     schedule.every(2).seconds.do(saveImageSchedule)
        # if key == 27: # exit on ESC
        #     saveImage(frame)
        #     break

""" 
    Current times is for 2 seconds. Hence, the program will wake up after every 2 seconds and take a screenshot.
"""
schedule.every(2).seconds.do(launchWebcamAndTakeScreenshot)
while True: 
    schedule.run_pending()
    time.sleep(1)
