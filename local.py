import cv2
import numpy as np

def edge_linking(image, mag_threshold, angle_threshold, gap_length):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Compute gradients
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # Compute gradient magnitude and angle
    mag = np.sqrt(sobelx**2 + sobely**2)
    angle = np.arctan2(sobely, sobelx) * 180 / np.pi
    
    # Thresholding based on magnitude and angle
    binary = ((mag > mag_threshold) & (np.abs(angle) < angle_threshold)).astype(np.uint8) * 255
    
    # Scan rows and fill gaps
    for i in range(binary.shape[0]):
        gap_start = None
        for j in range(binary.shape[1]):
            if binary[i, j] == 0:
                if gap_start is None:
                    gap_start = j
            elif gap_start is not None and j - gap_start <= gap_length:
                binary[i, gap_start:j] = 255
                gap_start = None
                
    # Rotate the binary image by 90 degrees
    rotated_binary = np.rot90(binary)
    
    # Scan rows and fill gaps in rotated image
    for i in range(rotated_binary.shape[0]):
        gap_start = None
        for j in range(rotated_binary.shape[1]):
            if rotated_binary[i, j] == 0:
                if gap_start is None:
                    gap_start = j
            elif gap_start is not None and j - gap_start <= gap_length:
                rotated_binary[i, gap_start:j] = 255
                gap_start = None
    
    # Rotate back the binary image
    binary = np.rot90(rotated_binary, -1)
    
    return binary

# Load image
image = cv2.imread('lena.jpeg')

# Set thresholds and gap length
mag_threshold = 100
angle_threshold = 30
gap_length = 25

# Perform edge linking
result = edge_linking(image, mag_threshold, angle_threshold, gap_length)

# Convert the result to black and white (binary)
_, binary_result = cv2.threshold(result, 127, 255, cv2.THRESH_BINARY)

# Display the result
cv2.imshow('Edge Linked Image (Black and White)', binary_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
