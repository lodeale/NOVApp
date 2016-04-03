import cv2
import numpy as np

class Draw(object):

    def do(self,edges,img):
        #Take contours
        _,contours, hier = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #Define the areas
        areas = [cv2.contourArea(c) for c in contours]
        i=0
        for extension in areas:
            #If the area is heigher that 100, then this isn't a noise
            if extension > 100:
                cnt = contours[i]
                cv2.drawContours(img,[cnt],0,(0,0,255),2)
            i = i+1
        return img
