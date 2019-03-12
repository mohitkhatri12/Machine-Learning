# Importing libraries
import  cv2

# Deffining a function for detecting motion  
def    imageDifference(x,y,z):

        # Taking difference between frames	
	image1=cv2.absdiff(x,y)
	image2=cv2.absdiff(y,z)

        # Calculating differences in two frames
	finalDifference=cv2.bitwise_and(image1,image2)

        # Returning the frame with difference
	return  finalDifference


# Create a object of VideoCapture
# Use 0 if using the camera of laptop else 1
capture=cv2.VideoCapture(0)

# Taking 3 consistant frames
frame1=capture.read()[1]
frame2=capture.read()[1]
frame3=capture.read()[1]

# Converting them into grayscale
gray1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)

# Starting a infinite loop
while  capture.isOpened():
		# Passing arguments to above function
		image_difference=imageDifference(gray1,gray2,gray3)
		
		# Showing the fame with difference in 2 consecutive frames
		cv2.imshow('Difference',image_difference)

		# Capturing new frame
		status,frame=capture.read()
		
		# Showing the live video which is captured by the camera
		cv2.imshow("Normal",frame)

		# Swaping the frames with each other
		gray1=gray2
		gray2=gray3
		gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		# Writing code to close the windows
		if  cv2.waitKey(1) &  0xFF  ==  ord('q'):
			break
# destroying all the opened windows
cv2.destroyAllWindows()
capture.release()
