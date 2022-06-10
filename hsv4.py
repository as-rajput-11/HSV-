import cv2
import numpy as np
import matplotlib.pylab as plt
bck = cv2.imread("2.jpg")
img = cv2.imread("2.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (5, 75, 25), (25, 255, 255))
yellow = img.copy()
hsv[...,0] = hsv[...,0] + 20
yellow[imask] = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)[imask]
yellow = np.clip(yellow, 0, 255)
