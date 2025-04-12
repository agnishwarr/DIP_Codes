import cv2
import matplotlib.pyplot as plt
image = cv2.imread('pass.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Black and White Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.show()
