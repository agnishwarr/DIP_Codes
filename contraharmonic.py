import cv2
import numpy as np
def spatial_filtering(image, filter):
    output = np.zeros(image.shape)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            part = image[i - 1: i + filter.shape[0] - 1, j - 1: j + filter.shape[1] - 1]
            #Q = 1 # to remove pepper noise
            Q = -1 # to remove salt noise (ie) HMF, cannot do both simultaneously,
            #Q = 0 # works like A(rithmetic)MF
            numerator = denominator = 0
            for x in range(filter.shape[0]):
                for y in range(filter.shape[1]):
                    if Q > 0:
                        if part[x, y] != 0:
                            numerator += (part[x, y] ** (Q + 1))
                            denominator += (part[x, y] ** Q)
                    else:
                        if part[x, y] != 0:
                            inverse_value = 1.0 / part[x, y]
                            numerator += inverse_value ** -(Q + 1)
                            denominator += inverse_value ** -Q
            if denominator != 0:
                val = numerator / denominator
            else:
                val = 0
            output[i, j] = val
    return output
def add_impulse_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy_image = np.copy(image)
    # Add salt noise
    noisy_image[np.random.rand(*image.shape) < salt_prob] = 255
    # Add pepper noise
    noisy_image[np.random.rand(*image.shape) < pepper_prob] = 0
    return noisy_image
filter = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])
image = cv2.imread("home.jpg", cv2.IMREAD_GRAYSCALE)
noisy_image = add_impulse_noise(image)
out = spatial_filtering(noisy_image, filter)
out = out.astype(np.uint8)
cv2.imshow("Original", image)
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Filtered Image", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
