import cv2
import numpy as np
img = cv2.imread("lena.jpeg", 0)
def roberts(image, filter):
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
gx = roberts(img, np.array([[-1, 0], [0, 1]]))
gy = roberts(img, np.array([[0, -1], [1, 0]]))
out = np.sqrt(np.square(gx) + np.square(gy))
out = out.astype(np.uint8)
cv2.imshow("Input", img)
cv2.imwrite("gx Output of Roberts.png", gx)
cv2.imwrite("gy Output of Roberts.png", gy)
cv2.imwrite("Sharpen Output of Roberts.png", out)
cv2.waitKey(0)
cv2.destroyAllWindows()