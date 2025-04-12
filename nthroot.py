import numpy as np
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('Lena.jpeg', cv2.IMREAD_GRAYSCALE)
degrees = [2, 3, 4] 
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Lena')
plt.axis('off')
for i, n in enumerate(degrees, start=2):
    nth_root_image = np.power(image, 1/n)
    nth_root_image = np.clip(nth_root_image, 0, 255).astype(np.uint8)
    plt.subplot(1, 4, i)
    plt.imshow(nth_root_image, cmap='gray')
    plt.title(f'{n}th Root Lena')
    plt.axis('off')

plt.show()
