import cv2
import numpy as np
import matplotlib.pyplot as plt
def gaussian_kernel(kernel_size, sigma):
    kernel = np.fromfunction(lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x-(kernel_size-1)/2)**2 + (y-(kernel_size-1)/2)**2)/(2*sigma**2)), (kernel_size, kernel_size))
    return kernel / np.sum(kernel)
def gaussian_filter(image, kernel_size, sigma):
    kernel = gaussian_kernel(kernel_size, sigma)
    gaussian_image = cv2.filter2D(image, -1, kernel)
    return gaussian_image
image = cv2.imread('home.jpg', cv2.IMREAD_GRAYSCALE)
noisy_image = cv2.add(image, np.random.normal(0, 20, image.shape), dtype=cv2.CV_8UC1)
denoised_image = gaussian_filter(noisy_image, kernel_size=5, sigma=1)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(denoised_image, cmap='gray')
plt.title('Denoised Image (Gaussian Filter)')
plt.axis('off')
plt.show()
