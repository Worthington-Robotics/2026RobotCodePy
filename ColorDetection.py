
  #Modified from geeksforgeeks.org
  #Modified from opencv.org

  # Python code for Multiple Color Detection 


import numpy as np 
import cv2 


	# Capturing video through webcam 
cap = cv2.VideoCapture(0) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,0)
frame_centre_x = 0 

params = cv2.SimpleBlobDetector_Params()
detector = cv2.SimpleBlobDetector_create(params)
...
    #detector = cv2.SimpleBlobDetector_create(params)

	# Start a while loop 
while True: 
	
	# Reading the video from the 
	# webcam in image frames 

	#_, imageFrame = webcam.read() 
	ret, imageFrame = cap.read()

	if not ret:
		print("Failed to grab frame ")
		continue
	

	# Convert the imageFrame in 
	# BGR(RGB color space) to 
	# HSV(hue-saturation-value) 
	# color space 

	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
	#hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

	# Set range for yellow color and 
	# define mask 
	fuel_upper = np.array([120, 255, 255], np.uint8) 
	fuel_lower = np.array([20, 100, 80], np.uint8) 
	fuel_mask = cv2.inRange(hsvFrame, fuel_lower, fuel_upper) 

	
	# Morphological Transform, Dilation 
	# for each color and bitwise_and operator 
	# between imageFrame and mask determines 
	# to detect only that particular color 
	kernel = np.ones((5, 5), "uint8") 
	
	# For yellow color 
	fuel_mask = cv2.dilate(fuel_mask, kernel) 
	res_fuel = cv2.bitwise_and(imageFrame, imageFrame, 
		mask = fuel_mask) 
	


	#params.minThreshold = 0
	#params.maxThreshold = 60
	#params.minRepeatability = 0

	params.filterByColor = True
	params.blobColor = 255

	params.filterByArea = True
	params.minArea = 10
	
	params.filterByCircularity = True
	params.minCircularity = 0.1

	params.filterByConvexity = True
	params.minConvexity = 0.87

	params.filterByInertia = True 
	params.minInertiaRatio = 0.01


	keypoints = detector.detect(fuel_mask)

	drawBlobs = cv2.drawKeypoints(imageFrame, keypoints, np.array([]), (0,0,255),
		cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


			
	# Program Termination 
	cv2.imshow("Fuel Detection in Real-TIme", drawBlobs) 
	if cv2.waitKey(10) & 0xFF == ord('q'): 
		webcam.release() 
		cv2.destroyAllWindows() 
		break

	cv2.imshow("Mask", fuel_mask)


	largest_blob = 0 
	largest_size = 0

	for kp in keypoints:
		if kp.size > largest_size:
			largest_size = kp.size()
			largest_blob = kp

	if largest_blob is not None: 
		x, y = largest_blob.pt
		diameter = largest_blob.size

		offset = x - frame_centre_x
		cv2.circle(imageFrame, (int(x), int(y)), 5, (0,0,255), -1)


