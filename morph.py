import cv2
import numpy as np
import matplotlib.pyplot as plt
def erode(img, kernel):
    output = np.zeros_like(img)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            neighborhood = img[i - 1:i + 2, j - 1:j + 2]
            result = np.logical_and(neighborhood, kernel)
            # print(result)
            if np.all(result):
                output[i, j] = 255
    return output
def dilate(img, kernel):
    output = np.zeros_like(img)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            neighborhood = img[i - 1:i + 2, j - 1:j + 2]
            result = np.logical_and(neighborhood, kernel)
            if np.any(result):
                output[i, j] = 255
    return output
def opening(image, kernel):
    result = erode(image, kernel)
    result = dilate(result, kernel)
    return result
def closing(image, kernel):
    result = dilate(image, kernel)
    result = erode(result, kernel)
    return result
img = cv2.imread("morph.png", 0)
se = np.ones((3,3), np.uint8)
result_erode = erode(img, se)
result_dilate = dilate(img, se)
result_opening = opening(img, se)
result_closing = closing(img, se)
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.subplot(2, 3, 2)
plt.imshow(result_dilate, cmap='gray')
plt.title('Dilated Image')
plt.subplot(2, 3, 3)
plt.imshow(result_erode, cmap='gray')
plt.title('Eroded Image')
plt.subplot(2, 3, 4)
plt.imshow(result_opening, cmap='gray')
plt.title('Opening Image')
plt.subplot(2, 3, 5)
plt.imshow(result_closing, cmap='gray')
plt.title('Closing Image')
plt.tight_layout()
plt.show()
