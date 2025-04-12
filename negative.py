import cv2
import matplotlib.pyplot as plt
img_input = cv2.imread("lena.jpeg")
img_output = 255 - img_input
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB))
plt.title('Input Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB))
plt.title('Negative Image')
plt.axis('off')
plt.show()
