import cv2
from pil import  Image
import os

def getImagesCount(): 
    DIR = os.getcwd() + "/images"    
    count = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) + 1
    return count

def saveImage(frame):
    imageName = "image_" + str(getImagesCount()) + ".png"
    if not cv2.imwrite(os.getcwd() + "/images/" + imageName, frame):
        raise Exception("Could not write image")

def launch_webcam():     
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        img = Image.fromarray(frame)        
    else:
        rval = False
    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            saveImage(frame)
            break
    cv2.destroyWindow("preview")
    
launch_webcam()
