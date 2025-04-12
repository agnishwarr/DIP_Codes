import numpy as np
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('Lena.jpeg', cv2.IMREAD_GRAYSCALE)
anti_log_image = np.exp(image)
anti_log_image = np.clip(anti_log_image, 0, 255).astype(np.uint8)
cv2.imwrite('anti_log_Lena.jpeg', anti_log_image)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Lena')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(anti_log_image, cmap='gray')
plt.title('Anti-Log Lena')
plt.axis('off')
plt.show()
