import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("lena.jpeg", 0)
def prewitt(image, filter):
    output = np.zeros(image.shape)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            part = image[i - 1: i + filter.shape[0] - 1, j - 1: j + filter.shape[1] - 1]
            val = 0
            for k in range(filter.shape[0]):
                for l in range(filter.shape[1]):
                    val += (filter[k][l] * part[k][l])
            output[i][j] = int(val)
    return output
gx = prewitt(img, np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]))
gy = prewitt(img, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
out = np.sqrt(np.square(gx) + np.square(gy))
out = out.astype(np.uint8)
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Input Image')
plt.subplot(2, 2, 2)
plt.imshow(gx, cmap='gray')
plt.title('gx Output of Prewitt')
plt.subplot(2, 2, 3)
plt.imshow(gy, cmap='gray')
plt.title('gy Output of Prewitt')
plt.subplot(2, 2, 4)
plt.imshow(out, cmap='gray')
plt.title('Sharpen Output of Prewitt')
plt.show()
