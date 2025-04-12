import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('home.jpg', cv2.IMREAD_GRAYSCALE)

# Roberts Cross operator implementation without using inbuilt functions
def roberts_cross_without_inbuilt(image):
    # Roberts Cross kernels
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])

    # Convolve the image with the kernels
    grad_x = np.zeros_like(image, dtype=np.float32)
    grad_y = np.zeros_like(image, dtype=np.float32)
    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] - 1):
            grad_x[i, j] = image[i, j] * kernel_x[0, 0] + image[i, j + 1] * kernel_x[0, 1] + \
                           image[i + 1, j] * kernel_x[1, 0] + image[i + 1, j + 1] * kernel_x[1, 1]
            grad_y[i, j] = image[i, j] * kernel_y[0, 0] + image[i, j + 1] * kernel_y[0, 1] + \
                           image[i + 1, j] * kernel_y[1, 0] + image[i + 1, j + 1] * kernel_y[1, 1]

    # Compute gradient magnitude
    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    
    # Normalize gradient magnitude
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    return gradient_magnitude

# Compute Roberts Cross gradient without using inbuilt functions
gradient_roberts_without_inbuilt = roberts_cross_without_inbuilt(image)

# Plotting the original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Plotting the Roberts Cross gradient
plt.subplot(1, 2, 2)
plt.imshow(gradient_roberts_without_inbuilt, cmap='gray')
plt.title('Roberts Cross (without inbuilt)')
plt.axis('off')

plt.show()
