import cv2
import numpy as np
import matplotlib.pyplot as plt
def average_filter(image, kernel_size):
    # Define a kernel with all values equal to 1
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)
    # Perform convolution with the average kernel
    return cv2.filter2D(image, -1, kernel)
def weighted_average_filter(image, kernel_size, weights):
    # Ensure the length of the weights array matches the total number of elements in the kernel
    assert len(weights) == kernel_size * kernel_size, "Length of weights should match kernel size"
    kernel = np.array(weights, dtype=np.float32).reshape(kernel_size, kernel_size)
    kernel = kernel / np.sum(kernel)
    return cv2.filter2D(image, -1, kernel)
image = cv2.imread('home.jpg', cv2.IMREAD_GRAYSCALE)
kernel_size = 3
average_filtered_image = average_filter(image, kernel_size)
weights = [1, 2, 1,
           2, 4, 2,
           1, 2, 1]
weighted_average_filtered_image = weighted_average_filter(image, kernel_size, weights)
plt.figure(figsize=(12, 8))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(average_filtered_image, cmap='gray')
plt.title('Average Filter')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(weighted_average_filtered_image, cmap='gray')
plt.title('Weighted Average Filter')
plt.axis('off')
plt.show()
