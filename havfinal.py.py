import cv2
import numpy as np
img = cv2.imread(r'1.jpg')
img = cv2.resize(img, (320,280))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def null(x):
    pass

cv2.namedWindow('HSV')
cv2.createTrackbar("Hue", "HSV", 0, 180, null)
cv2.createTrackbar("sat", "HSV", 0, 100, null)
cv2.createTrackbar("val", "HSV", 0, 100, null)


while True:
    hue = cv2.getTrackbarPos('Hue','HSV')
    sat = cv2.getTrackbarPos('sat','HSV')
    val = cv2.getTrackbarPos('val','HSV')
    #img = cv2.imread(r'1.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]

    # h=hsv[0]
    # s=hsv[1]
    # v=hsv[2]


    hnew = cv2.add(h, hue)
    snew = cv2.add(s,sat)
    vnew = cv2.add(v,val)
    #vnew = cv2.add(hsv[:,:,2], val, hsv[:,:,2])
    
    hsvnew = cv2.merge([hnew,snew,vnew])
    result = cv2.cvtColor(hsvnew, cv2.COLOR_HSV2BGR)
    cv2.imshow("Hue'd Image", result)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows() 
