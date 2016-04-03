import cv2
import numpy as np

class ProcessImage(object):

    def do(self,img):
        #Convert the image to GRAY
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #Better the contour and the border
        img = cv2.GaussianBlur(img, (5, 5), 0)
        canny = cv2.Canny(img,1,2)
        return canny
