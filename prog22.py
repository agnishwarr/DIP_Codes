import cv2
import numpy as np
import matplotlib.pyplot as plt
def inverse_translation(image, tx, ty):
    inv_trans_matrix = np.array([[1, 0, -tx], [0, 1, -ty], [0, 0, 1]])
    height, width = image.shape
    result_image = np.zeros_like(image)
    for x1 in range(width):
        for y1 in range(height):
            a = np.array([x1, y1, 1])
            original_cord = np.dot(inv_trans_matrix, a)
            x, y = original_cord[:2].astype(int)
            if 0 <= x < width and 0 <= y < height:
                result_image[y, x] = image[y1, x1]
    return result_image
image = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Unable to load the image.")
    exit()
result_image = inverse_translation(image, tx=100, ty=100)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(result_image, cmap='gray')
plt.title('Result Image')
plt.axis('off')
plt.show()
