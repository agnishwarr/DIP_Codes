import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
gamma_values = [0.5, 1.5, 2.5]
plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.axis('off')
for i, gamma in enumerate(gamma_values):
    gamma_corrected = np.uint8(cv2.pow(image / 255.0, gamma) * 255)
    plt.subplot(1, 4, i+2)
    plt.imshow(gamma_corrected, cmap='gray')
    plt.title('Gamma={}'.format(gamma))
    plt.axis('off')
plt.show()
