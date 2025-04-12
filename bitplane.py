import cv2
import numpy as np
import matplotlib.pyplot as plt
def bit_plane_slice(image):
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image
    bit_planes = []
    for bit in range(8):
        bit_plane = np.bitwise_and(gray_image, 2 ** bit)
        bit_plane = (bit_plane / (2 ** bit)) * 255
        bit_plane = np.uint8(bit_plane)
        bit_planes.append(bit_plane)
    return bit_planes
image = cv2.imread("Lena.jpeg")
if image is None:
    print("Error: Could not load the image.")
else:
    bit_planes = bit_plane_slice(image)
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')
    for i, bit_plane in enumerate(bit_planes, start=2):
        plt.subplot(3, 3, i)
        plt.imshow(bit_plane, cmap='gray')
        plt.title(f"Bit Plane {i-1}")
        plt.axis('off')
    plt.tight_layout()
    plt.show()
