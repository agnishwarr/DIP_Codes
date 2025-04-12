import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
c = 255 / np.log(1 + np.max(image))
log_transformed_image = c * (np.log(image + 1))
log_transformed_image = np.uint8(log_transformed_image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(log_transformed_image, cmap='gray')
plt.title('Log Transformed Image')
plt.axis('off')
plt.show()
