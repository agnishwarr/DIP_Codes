import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('home.jpg', cv2.IMREAD_GRAYSCALE)
def add_impulse_noise(image, prob):
    noisy_image = np.copy(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if np.random.rand() < prob:
                noisy_image[i, j] = 0 if np.random.rand() < 0.5 else 255
    return noisy_image
def median_filter(image, kernel_size):
    padded_image = np.pad(image, ((kernel_size//2, kernel_size//2), (kernel_size//2, kernel_size//2)), mode='edge')
    filtered_image = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            neighbors = padded_image[i:i+kernel_size, j:j+kernel_size]
            filtered_image[i, j] = np.median(neighbors)
    return filtered_image
noisy_image = add_impulse_noise(image, prob=0.1)
denoised_image = median_filter(noisy_image, kernel_size=3)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(denoised_image, cmap='gray')
plt.title('Denoised Image (Median Filter)')
plt.axis('off')
plt.show()
