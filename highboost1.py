import numpy as np
import cv2

def high_boost_filtering(image, k=1.5, scaling_factor=1):
    # Define the kernel for high-pass filtering
    kernel = np.array([[-1, -1, -1],
                       [-1, k, -1],
                       [-1, -1, -1]])

    # Apply the kernel using convolution
    filtered_image = cv2.filter2D(image, -1, kernel)

    # Apply scaling to the high-pass filtered image
    scaled_filtered_image = scaling_factor * filtered_image

    # Combine the original image with the scaled high-pass filtered image
    sharpened_image = cv2.add(image, scaled_filtered_image)

    return sharpened_image

# Read the image
image = cv2.imread('lena.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply high-boost filtering with scaling
sharpened_image = high_boost_filtering(gray_image, k=9, scaling_factor=1)

# Display the original and sharpened images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
