import cv2
import numpy as np
import matplotlib.pyplot as plt
def sobel_operator(image):
    kernel_x = np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
    
    kernel_y = np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]])
    gradient_x = cv2.filter2D(image, cv2.CV_64F, kernel_x)
    gradient_y = cv2.filter2D(image, cv2.CV_64F, kernel_y)
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    return gradient_x.astype(np.uint8), gradient_y.astype(np.uint8), gradient_magnitude.astype(np.uint8)
img = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)
sobel_x, sobel_y, combined_edge = sobel_operator(img)
plt.figure(figsize=(20, 5))
plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel Edge (X-direction)')
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel Edge (Y-direction)')
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(combined_edge, cmap='gray')
plt.title('Combined Sobel Edge')
plt.axis('off')
plt.tight_layout()
plt.show()
