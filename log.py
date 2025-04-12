import cv2
import numpy as np

def padding(image, pad_width):
    height, width = image.shape
    new_height = height + 2 * pad_width
    new_width = width + 2 * pad_width

    result_image = np.zeros((new_height, new_width), dtype=image.dtype)

    result_image[pad_width:new_height - pad_width, pad_width:new_width - pad_width] = image

    return result_image

def apply_mask(image, mask):
    pad_width = mask.shape[0] // 2
    padded_image = padding(image, pad_width)
    result_image = np.zeros_like(image)

    for i in range(pad_width, len(padded_image) - pad_width):
        for j in range(pad_width, len(padded_image[0]) - pad_width):
            window = padded_image[i - pad_width:i + pad_width + 1, j - pad_width:j + pad_width + 1]
            result_window = np.sum(window * mask)
            # Clip the result to the valid range of the data type
            result_image[i - pad_width, j - pad_width] = np.clip(round(result_window), 0, 255)

    return result_image

image = cv2.imread("home.jpg", 0)
mask = np.array([[1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]])

result_image = apply_mask(image, mask)


convolved_image = np.zeros_like(image)
convolved_image = result_image * image

mask2 = np.array([[1, 1, 1],    
                  [1, -8, 1],
                  [1, 1, 1]])

smoothed_image = apply_mask(convolved_image, mask2)


import matplotlib.pyplot as plt
plt.subplot(2, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(2, 4, 2)
plt.imshow(result_image, cmap='gray')
plt.title('Result Image(Gaussian)')
plt.subplot(2, 4, 3)
plt.imshow(convolved_image, cmap='gray')
plt.title('Convolved Image')
plt.subplot(2, 4, 4)
plt.imshow(smoothed_image, cmap='gray')
plt.title('Final Image')
plt.show()