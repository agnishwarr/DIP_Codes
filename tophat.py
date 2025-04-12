import cv2
import numpy as np

# Read the image
image = cv2.imread('pass.jpg')

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Perform morphological operations to clean up the mask
kernel = np.ones((5,5), np.uint8)
mask = cv2.erode(mask, kernel, iterations=1)
mask = cv2.dilate(mask, kernel, iterations=1)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:  # adjust threshold as needed
        cv2.drawContours(image, [contour], -1, (0,255,0), 3)

# Display the original image with detected contours
cv2.imshow('Detected Ball', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
