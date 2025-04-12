import cv2
import numpy as np
import matplotlib.pyplot as plt
def spatial_filtering(image, filter):
    output = np.zeros(image.shape)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            part = image[i - 1: i + filter.shape[0] - 1, j - 1: j + filter.shape[1] - 1]
            val = 0
            for x in range(filter.shape[0]):
                for y in range(filter.shape[1]):
                    if part[x, y] == 0:
                        continue
                    val += 1 / part[x, y]
            if val == 0:
                continue
            val = (filter.shape[0] * filter.shape[1]) / val
            output[i, j] = val
    return output
# Define the harmonic filter
filter = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])
# Read the original image
img = cv2.imread("lena.jpeg", 0)
# Add salt noie
salt_noise = np.zeros(img.shape, np.uint8)
cv2.randu(salt_noise, 0, 255)
salt_mask = salt_noise > 240
img_salt = img.copy()
img_salt[salt_mask] = 255
"""# Add pepper noise
pepper_noise = np.zeros(img.shape, np.uint8)
cv2.randu(pepper_noise, 0, 255)
pepper_mask = pepper_noise < 15"""
img_sp = img_salt.copy()
#img_sp[pepper_mask] = 0
out = spatial_filtering(img_sp, filter)
out = out.astype(np.uint8)
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(img_salt, cmap='gray')
plt.title("Salt Noise")
plt.axis('off')
"""plt.subplot(1, 4, 3)
plt.imshow(img_sp, cmap='gray')
plt.title("Pepper Noise")
plt.axis('off')"""
plt.subplot(1, 4, 4)
plt.imshow(out, cmap='gray')
plt.title("Harmonic Filtered")
plt.axis('off')
plt.show()
