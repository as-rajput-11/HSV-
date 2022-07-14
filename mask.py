
import numpy as np
import cv2
 
#Create the circle
colour = (0,255,0)
lineWidth = 3       #-1 will result in filled circle
radius = 0
point = (0,0)

#function for detecting left mouse click
def click(event, x,y, flags, param):
    global point, pressed
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Pressed", x,y)
        point = (x,y)
        return point
         
#event handler
cv2.namedWindow("Frame")      #must match the imshow 1st argument
     
 
 
cap = cv2.VideoCapture(0)
mask_Cir = []
#Loop for video stream
while (True):
     
    stream = cv2.waitKey(20)   #Load video every 1ms and to detect user entered key
     
    #Read from videoCapture stream and display
    ret,frame = cap.read()
    cv2.setMouseCallback("Frame", click)
    
    mask = np.zeros(frame.shape, dtype=np.uint8)
    # pressed = cv2.circle(mask, (10,20), 5300, (255,255,255), -1)
    # aaa = (50,55) 
    mask_Cir.append(point)
    for i in mask_Cir:
        mask = cv2.circle(mask,i, 50, (255,255,255), -1) 
        result = cv2.bitwise_or(frame, mask)
        cv2.imshow('Frame', result)
        # aaa = (150,170)
        

    # # # Mask input image with binary mask

    # # # Color background white
    # result[mask==0] = 255 # Optional

    # #Display the resulting frame
    # cv2.circle(frame, point,radius,colour,lineWidth)     #circle properties as arguments
    # frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)  #this fx,fy value will be explained in post
    # cv2.imshow("Frame", frame)
     
    if stream & 0XFF == ord('q'):  #If statement to stop loop,Letter 'q' is the escape key
        break                      #get out of loop
         
cap.release()
cv2.destroyAllWindows()
