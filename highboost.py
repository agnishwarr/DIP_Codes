import numpy as np
import cv2

def convolve(image, kernel):
    # Get the dimensions of the image and the kernel
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate the padding size
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Create an empty array to store the convolved image
    convolved_image = np.zeros_like(image)

    # Pad the image
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    # Perform convolution
    for i in range(image_height):
        for j in range(image_width):
            convolved_image[i, j] = np.sum(padded_image[i:i+kernel_height, j:j+kernel_width] * kernel)

    return convolved_image

def high_boost_filtering(image, k=1.5, scaling_factor=1):
    # Define the kernel for high-pass filtering
    kernel = np.array([[-1, -1, -1],
                       [-1, k, -1],
                       [-1, -1, -1]])

    # Apply the kernel using convolution
    filtered_image = convolve(image, kernel)

    # Apply scaling to the high-pass filtered image
    scaled_filtered_image = scaling_factor * filtered_image

    # Combine the original image with the scaled high-pass filtered image
    sharpened_image = image + scaled_filtered_image

    return sharpened_image

# Read the image
image = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply high-boost filtering with scaling
sharpened_image = high_boost_filtering(image, k=1, scaling_factor=1)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
