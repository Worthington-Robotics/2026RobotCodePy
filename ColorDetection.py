class ColorDetection:
  #Modified from geeksforgeeks.org
  #Modified from opencv.org

  # Python code for Multiple Color Detection 


	import numpy as np 
	import cv2 


	# Capturing video through webcam 
	webcam = cv2.VideoCapture(0) 

	# Start a while loop 
	while(1): 
	
	# Reading the video from the 
	# webcam in image frames 
		_, imageFrame = webcam.read() 

	# Convert the imageFrame in 
	# BGR(RGB color space) to 
	# HSV(hue-saturation-value) 
	# color space 
		hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

	# Set range for yellow color and 
	# define mask 
		fuel_lower = np.array([136, 87, 111], np.uint8) 
		fuel_upper = np.array([180, 255, 255], np.uint8) 
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
	

		params = cv2.SimpleBlobDetector_Params()

		params.minThreshold = 0
		params.maxThreshold = 0

		params.filterByArea = True
		params.minArea = 10
	
		params.filterByCircularity = True
		params.minCircularity = 0.1

		params.filterByConvexity = True
		params.minConvexity = 0.87

		params.filterByInertia = True 
		params.minInertiaRatio = 0.01

		detector = cv2.SimpleBlobDetector_create(params)

		keypoints = detector.detect(imageFrame)

		drawBlobs = cv2.drawKeypoints(imageFrame, keypoints, np.array([]), (0,0,255),
			cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


			
	# Program Termination 
		cv2.imshow("Fuel Detection in Real-TIme", drawBlobs) 
		if cv2.waitKey(10) & 0xFF == ord('q'): 
			webcam.release() 
			cv2.destroyAllWindows() 
			break

