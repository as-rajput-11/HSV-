import cv2
import numpy as np
img = cv2.imread(r'2.jpg')
img = cv2.resize(img, (320,280))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def null(x):
    pass

cv2.namedWindow('HSV')
cv2.createTrackbar("Hue", "HSV", 0, 180, null)

while True:
    hue = cv2.getTrackbarPos('Hue','HSV')
    img = cv2.imread(r'C:\\Abdul\\WhatsApp.jpeg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]
    hnew = cv2.add(h, hue)
    hsvnew = cv2.merge([hnew,s,v])
    result = cv2.cvtColor(hsvnew, cv2.COLOR_HSV2BGR)
    cv2.imshow("Hue'd Image", result)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows() 
