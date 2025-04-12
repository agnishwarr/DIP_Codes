import cv2
import numpy as np

# Read the input image
image = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)

# Check if the image was read successfully
if image is None:
    print("Error: Unable to read the input image.")
    exit()

# Define the probability of pepper noise
pepper_prob = 0.01

# Generate pepper noise
pepper_mask = np.random.random(image.shape) < pepper_prob
image[pepper_mask] = 0  # Set pepper noise (black pixels)

# Define the kernel size for the median filter
kernel_size = 5

# Define the padding size
padding = kernel_size // 2

# Get the height and width of the image
height, width = image.shape

# Create an empty array for the smoothed image
smoothed_image = np.zeros_like(image)

# Apply the median filter
for i in range(padding, height - padding):
    for j in range(padding, width - padding):
        # Extract the neighborhood around the current pixel
        neighborhood = image[i - padding:i + padding + 1, j - padding:j + padding + 1]
        # Apply the median operation
        median_value = np.median(neighborhood)
        # Assign the median value to the corresponding pixel in the smoothed image
        smoothed_image[i, j] = median_value

# Display the original, noisy (with pepper noise), and smoothed images
cv2.imshow("Original Image", image)
cv2.imshow("Noisy Image (with Pepper Noise)", cv2.cvtColor(image, cv2.COLOR_GRAY2BGR))  # Convert to BGR for visualization
cv2.imshow("Smoothed Image", smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
