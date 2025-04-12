import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('home.jpg', cv2.IMREAD_GRAYSCALE)

# Compute gradients using Sobel operators
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute gradient magnitude
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Compute gradient angle using arctan2
gradient_angle = np.arctan2(gradient_y, gradient_x)

# Plotting all components in the same plot
plt.figure(figsize=(15, 12))

# Original image
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Gradient in the x-direction
plt.subplot(2, 3, 2)
plt.imshow(gradient_x, cmap='gray')
plt.title('Gradient in X-direction')
plt.axis('off')

# Gradient in the y-direction
plt.subplot(2, 3, 3)
plt.imshow(gradient_y, cmap='gray')
plt.title('Gradient in Y-direction')
plt.axis('off')

# Gradient magnitude
plt.subplot(2, 3, 4)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Gradient Magnitude')
plt.axis('off')

# Gradient angle
plt.subplot(2, 3, 5)
plt.imshow(gradient_angle, cmap='gray')
plt.title('Gradient Angle')
plt.axis('off')

plt.tight_layout()
plt.show()
