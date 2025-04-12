import cv2
import numpy as np
import matplotlib.pyplot as plt
def correlation(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    output = np.zeros_like(image)
    for i in range(image_height - kernel_height + 1):
        for j in range(image_width - kernel_width + 1):
            output[i, j] = np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel)
    return output
def convolution(image, kernel):
    kernel_height, kernel_width = kernel.shape
    flipped_kernel = np.zeros_like(kernel)
    for i in range(kernel_height):
        for j in range(kernel_width):
            flipped_kernel[i, j] = kernel[kernel_height - 1 - i, kernel_width - 1 - j]
    return correlation(image, flipped_kernel)
image = cv2.imread('home.jpg', cv2.IMREAD_GRAYSCALE)
kernel = np.array([[0, 0, 0],
                   [0, 1, 0],
                   [0, 0, 0]])
correlation_result = correlation(image, kernel)
print("Correlation Result:")
print(correlation_result)
convolution_result = convolution(image, kernel)
print("\nConvolution Result:")
print(convolution_result)
plt.figure(figsize=(10, 5))
plt.subplot(3,2, 1)
plt.imshow(correlation_result, cmap='gray')
plt.title('Correlation Result')
plt.axis('off')
plt.subplot(3, 2, 2)
plt.imshow(convolution_result, cmap='gray')
plt.title('Convolution Result')
plt.axis('off')
plt.subplot(3,2,3)
plt.imshow(image,cmap="gray")
plt.title("Original")
plt.axis("off")
plt.show()
