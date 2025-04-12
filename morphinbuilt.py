import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("morph.png", 0)

# Define the kernel
kernel = np.ones((3, 3), np.uint8)

# Apply morphological operations
result_dilate = cv2.dilate(img, kernel, iterations=1)
result_erode = cv2.erode(img, kernel, iterations=1)
result_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
result_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow(result_dilate, cmap='gray')
plt.title('Dilated Image')

plt.subplot(2, 3, 3)
plt.imshow(result_erode, cmap='gray')
plt.title('Eroded Image')

plt.subplot(2, 3, 4)
plt.imshow(result_opening, cmap='gray')
plt.title('Opening Image')

plt.subplot(2, 3, 5)
plt.imshow(result_closing, cmap='gray')
plt.title('Closing Image')

plt.tight_layout()
plt.show()
