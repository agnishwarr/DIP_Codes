import cv2
import numpy as np
import matplotlib.pyplot as plt
a = np.zeros((500, 500), dtype=int)
r = len(a) // 2
c = len(a[0]) // 2
for i in range((r - 35), (r - 15)):
    for j in range((c - 35), (c + 35)):
        a[i][j] = 255
for i in range((r - 15), (r + 35)):
    for j in range((c - 10), (c + 10)):
        a[i][j] = 255
sf=float(input("Enter shear factor: ")) 
shm = np.array([[1, sf, -sf*r], [0, 1, 0]])
sh = cv2.warpAffine(np.uint8(a), shm, (500, 500))
svm = np.array([[1, 0, 0], [sf, 1, -sf*c]])
sv = cv2.warpAffine(np.uint8(a), svm, (500, 500))
plt.figure(figsize=(10, 5))
plt.subplot(3, 1, 1)
plt.imshow(a, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(3, 1, 2)
plt.imshow(sh, cmap='gray')
plt.title('Horizontal Shearing')
plt.axis('off')
plt.subplot(3, 1, 3)
plt.imshow(sv, cmap='gray')
plt.title('Vertical Shearing')
plt.axis('off')
plt.show()

