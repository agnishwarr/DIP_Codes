import cv2
import numpy as np
def laplacian(image, filter):
    output = np.zeros(image.shape)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            part = image[i - 1: i + filter.shape[0] - 1, j - 1: j + filter.shape[1] - 1]
            val = 0
            for x in range(filter.shape[0]):
                for y in range(filter.shape[1]):
                    val += (filter[x][y] * part[x][y])
            output[i][j] = int(val)
    return output
img = cv2.imread("lena.jpeg", 0)
out4 = laplacian(img, filter=np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]))
out8 = laplacian(img, filter=np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]))
out4 = out4.astype(np.uint8)
out8 = out8.astype(np.uint8)
cv2.imshow("Input", img)
cv2.imwrite("Laplacian Output of eye -4.png", out4)
cv2.imwrite("Laplacian Output of eye -8.png", out8)
cv2.waitKey(0)
cv2.destroyAllWindows()