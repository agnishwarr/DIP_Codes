import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x-size//2)**2 + (y-size//2)**2)/(2*sigma**2)), (size, size))
    return kernel / np.sum(kernel)

def convolution(image, kernel):
    # Pad the image to handle boundaries
    padded_image = np.pad(image, ((kernel.shape[0]//2, kernel.shape[0]//2), (kernel.shape[1]//2, kernel.shape[1]//2)), mode='constant')

    # Initialize output image
    output = np.zeros_like(image)

    # Perform convolution
    for y in range(kernel.shape[0]//2, padded_image.shape[0] - kernel.shape[0]//2):
        for x in range(kernel.shape[1]//2, padded_image.shape[1] - kernel.shape[1]//2):
            patch = padded_image[y - kernel.shape[0]//2:y + kernel.shape[0]//2 + 1, x - kernel.shape[1]//2:x + kernel.shape[1]//2 + 1]
            output[y - kernel.shape[0]//2, x - kernel.shape[1]//2] = np.sum(patch * kernel)

    return output

def difference_of_gaussians(image, sigma1, sigma2):
    kernel1 = gaussian_kernel(9, sigma1)
    kernel2 = gaussian_kernel(9, sigma2)
    blurred1 = convolution(image, kernel1)
    blurred2 = convolution(image, kernel2)
    return blurred1 - blurred2

image = cv2.imread("home.jpg", cv2.IMREAD_GRAYSCALE)
sigma1 = 1.68
sigma2 = 1.05
DoG_image = difference_of_gaussians(image, sigma1, sigma2)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(DoG_image, cmap='gray')
plt.title('Difference of Gaussian')

plt.show()
