import cv2
import numpy as np
import matplotlib.pyplot as plt
def add_salt_and_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy_image = np.copy(image)
    salt = np.random.rand(*image.shape) < salt_prob
    noisy_image[salt] = 255
    pepper = np.random.rand(*image.shape) < pepper_prob
    noisy_image[pepper] = 0
    return noisy_image
def min_filter(image, kernel_size):
    return cv2.erode(image, np.ones((kernel_size, kernel_size), np.uint8))
def max_filter(image, kernel_size):
    return cv2.dilate(image, np.ones((kernel_size, kernel_size), np.uint8))
image = cv2.imread("home.jpg", cv2.IMREAD_GRAYSCALE)
noisy_image = add_salt_and_pepper_noise(image)
min_filtered = min_filter(noisy_image, kernel_size=3)
max_filtered = max_filter(noisy_image, kernel_size=3)
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(min_filtered, cmap='gray')
plt.title('Minimum Filtered Image')
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(max_filtered, cmap='gray')
plt.title('Maximum Filtered Image')
plt.axis('off')
plt.tight_layout()
plt.show()
