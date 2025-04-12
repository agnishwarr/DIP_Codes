import cv2
import numpy as np
def spatial_filtering(image, filter):
    output = np.zeros(image.shape)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            part = image[i - 1: i + filter.shape[0] - 1, j - 1: j + filter.shape[1] - 1]
            log_sum = 0
            for x in range(filter.shape[0]):
                for y in range(filter.shape[1]):
                    if part[x, y] == 0:
                        continue
                    log_sum += np.log(part[x, y])

            val = np.exp(log_sum / (filter.shape[0] * filter.shape[1]))
            output[i, j] = val
    return output
filter = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])
img = cv2.imread("lena.jpeg", 0)
image = cv2.imread("lena.jpeg", 0)
mean = 0
stddev = 30
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)
img = cv2.add(img, noise)
out = spatial_filtering(img, filter)
out = out.astype(np.uint8)
cv2.imwrite("GeometricMean_Input.png", image)
cv2.imwrite("GeometricMean_Noise.png", img)
cv2.imwrite("GeometricMean_Output.png", out)
cv2.waitKey(0)
cv2.destroyAllWindows()