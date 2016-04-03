#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import cv2
import numpy as np
from lib.processImage import ProcessImage
from lib.draw import Draw

_KEY = 0
_RESOLUTION_X = 1200
_RESOLUTION_Y = 700

if __name__ == '__main__':
    #Take the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i","--image",required=True,help="Path to the image")
    args = ap.parse_args()
    #Save Image
    img = cv2.imread(args.image)
    #Process Image
    p = ProcessImage()
    edges = p.do(img)
    #Draw Image
    show = Draw()
    show.do(edges,img)

    #Show the Images
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.imshow('Original', img)
    cv2.resizeWindow('Original',_RESOLUTION_X,_RESOLUTION_Y)
    cv2.waitKey(_KEY)
    cv2.destroyAllWindows()

