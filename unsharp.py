import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('home.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
mask = gray_image - blurred_image
weight = 3
unsharp_masked_image = gray_image + weight * mask
unsharp_masked_image = cv2.normalize(unsharp_masked_image, None, 0, 255, cv2.NORM_MINMAX)
unsharp_masked_image = unsharp_masked_image.astype(np.uint8)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB))
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(unsharp_masked_image, cv2.COLOR_GRAY2RGB))
plt.title('Unsharp Masked Image (Weight = {})'.format(weight))
plt.axis('off')
plt.tight_layout()
plt.show()
