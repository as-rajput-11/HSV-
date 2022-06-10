from configparser import Interpolation
import cv2
from matplotlib import image
import numpy as np

def nothing(x):
    pass

# cap = cv2.VideoCapture("b.mp4")
image = cv2.imread('3.jpg')
image = cv2.resize(image, (580, 540),interpolation = cv2.INTER_NEAREST)




cv2.namedWindow('image')


cv2.createTrackbar('HMax', 'image', 0, 180, nothing)
cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
cv2.createTrackbar('VMax', 'image', -100, 100, nothing)





while(1):

    # _,image = cap.read()
  
  
    hMax = cv2.getTrackbarPos('HMax', 'image')
    sMax = cv2.getTrackbarPos('SMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')

    




    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]
    # image[image < 255-vMax] += vMax  
   


    hnew = cv2.add(h, hMax)
    snew = cv2.add(s,sMax)
    vnew = cv2.add(v,vMax)
    hsvnew = cv2.merge([hnew,snew,vnew])
    result = cv2.cvtColor(hsvnew, cv2.COLOR_HSV2BGR)
    cv2.imshow('image', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cap.release()
cv2.destroyAllWindows()





##########################################################################################################################



import cv2

def Brightness(brightness=0):
	
	
	brightness = cv2.getTrackbarPos('Brightness',
									'GEEK')
	effect = controller(img, brightness)

	cv2.imshow('Effect', effect)

def controller(img, brightness=255):

	brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

	if brightness != 0:

		if brightness > 0:

			shadow = brightness

			max = 255

		else:

			shadow = 0
			max = 255 + brightness

		al_pha = (max - shadow) / 255
		ga_mma = shadow

		
		cal = cv2.addWeighted(img, al_pha,
							img, 0, ga_mma)

	else:
		cal = img

	
	cv2.putText(cal, 'B:{}'.format(brightness,
										), (10, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

	return cal

if __name__ == '__main__':
	
	original = cv2.imread("2.jpg")
	original = cv2.resize(original, (580, 540),interpolation = cv2.INTER_NEAREST)
	
	img = original.copy()

	
	cv2.namedWindow('GEEK')

	
	cv2.imshow('GEEK', original)

	
	cv2.createTrackbar('Brightness',
					'GEEK', 255, 2 * 255,
					Brightness)
	

	
	Brightness()


cv2.waitKey(0)




