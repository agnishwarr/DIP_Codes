import numpy as np
import cv2 
def x_axis(image):
    result_image = np.zeros((image.shape[0], image.shape[1]), dtype = int)
    for i in range((image.shape[0])):
        for j in range(image.shape[1]-1):
            result_image[i,j] = int(image[i,j+1]) + int(image[i,j-1])- 2*int(image[i, j])
    return result_image
def y_axis(image):
    result_image = np.zeros((image.shape[0], image.shape[1]), dtype = int)
    for i in range((image.shape[0])-1):
        for j in range((image.shape[1])):
            result_image[i,j] = int(image[i+1,j]) + int(image[i-1,j]) - 2*int(image[i, j])
    return result_image
def second_derivative(image):
    result_image = np.zeros((image.shape[0], image.shape[1]), dtype = int)
    for i in range((image.shape[0])-1):
        for j in range((image.shape[1])-1):
            result_image[i,j] = int(image[i,j+1]) + int(image[i,j-1]) + int(image[i+1,j]) + int(image[i-1,j]) - 4*int(image[i, j])
    return result_image
image = cv2.imread('home.jpg',0)
gx = x_axis(image)
gy = y_axis(image)
result_image = abs(gx) + abs(gy)
result_image3 = second_derivative(image)
result_image2 = image + result_image
import matplotlib.pyplot as plt
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(2, 3, 2)
plt.imshow(gx, cmap='gray')
plt.title('X-axis Derivative')
plt.subplot(2, 3, 3)
plt.imshow(gy, cmap='gray')
plt.title('Y-axis Derivative')
plt.subplot(2, 3, 4)
plt.imshow(result_image, cmap='gray')
plt.title('Result Image(gx+gy)')
plt.subplot(2, 3, 5)
plt.imshow(result_image2, cmap='gray')
plt.title('final Image(original + result_image3')
plt.subplot(2, 3, 6)
plt.imshow(result_image3, cmap='gray')
plt.title('Second Derivative(directly)')
plt.show()