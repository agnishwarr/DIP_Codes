import cv2
import numpy as np
image = cv2.imread('morph.png', cv2.IMREAD_GRAYSCALE)
structuring_element = np.ones((3, 3), np.uint8)
def erode(img, kernel):
    output = np.zeros_like(img)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            neighborhood = img[i - 1:i + 2, j - 1:j + 2]
            result = np.logical_and(neighborhood, kernel)
            if np.all(result):
                output[i, j] = 255
    return output
eroded_image = erode(image, structuring_element)
boundary = cv2.subtract(image, eroded_image)
cv2.imshow('Original Image', image)
cv2.imshow('Boundary Extracted Image', boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
