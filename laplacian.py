import numpy as np
import cv2
def padding(image, pad_width):
    height,width = image.shape
    new_height = height + 2 * pad_width
    new_width = width + 2 * pad_width
    result_image = np.zeros((new_height, new_width), dtype=image.dtype)
    result_image[pad_width:new_height - pad_width, pad_width:new_width - pad_width] = image
    return result_image
def apply_mask(image, mask):
    pad_width = mask.shape[0] // 2
    padded_image = padding(image,pad_width)
    result_image = np.zeros_like(image, dtype = np.float32)
    for i in range(pad_width, len(padded_image) - pad_width):
        for j in range(pad_width, len(padded_image[0]) - pad_width):
            window = padded_image[i - pad_width:i + pad_width + 1, j - pad_width:j + pad_width + 1]
            result_image[i - pad_width, j - pad_width] = round(np.sum(window * mask))
    return result_image
image = cv2.imread("lena.jpeg", cv2.IMREAD_GRAYSCALE)
mask = np.array([[0,1,0],
                  [1,-4,1],
                  [0,1,0]])
result_image = apply_mask(image,mask)
import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1,2,2)
plt.imshow(result_image, cmap='gray')
plt.title("Result Image")
plt.show()