import cv2
import numpy as np

def nothing(x):
    pass


img = cv2.imread('5.png')
img = cv2.resize(img, (580, 540),interpolation = cv2.INTER_NEAREST)


# def brightness(img):
cv2.namedWindow('image')
cv2.createTrackbar('val', 'image', 100, 300, nothing)
cv2.createTrackbar('HMax', 'image', 0, 180, nothing)
cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
	
	



while True:



	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)


	
	hsv = np.array(hsv, dtype=np.float64)

	val = cv2.getTrackbarPos('val', 'image')
	SMax = cv2.getTrackbarPos('HMax', 'image')
	VMax = cv2.getTrackbarPos('SMax', 'image')
	


	val = val/100 # dividing by 100 to get in range 0-1.5

	# scale pixel values up or down for channel 1(Saturation)
	hsv[:, :, 1] = hsv[:, :, 1] * val
	hsv[:, :, 1][hsv[:, :, 1] > 255] = 255 # setting values > 255 to 255.
	# scale pixel values up or down for channel 2(Value)
	hsv[:, :, 2] = hsv[:, :, 2] * val
	hsv[:, :, 2][hsv[:, :, 2] > 255] = 255 # setting values > 255 to 255.



	hsv[:, :, 0] = hsv[:, :, 0] + SMax
	hsv[:, :, 0][hsv[:, :, 0] > 255] = 255


	hsv[:, :, 2] = hsv[:, :, 2] + VMax
	hsv[:, :, 2][hsv[:, :, 2] > 255] = 255


	hsv = np.array(hsv, dtype=np.uint8)

	


	res = cv2.cvtColor(hsv, cv2.COLOR_HLS2BGR)


	# cv2.imshow("original", img)
	cv2.imshow('image', res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
