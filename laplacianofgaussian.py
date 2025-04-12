import cv2
import numpy as np
import matplotlib.pyplot as plt

def log_edge_detection(image):
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Calculate Laplacian
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

    # Suppress non-maximum values
    suppressed = np.zeros(laplacian.shape, dtype=np.uint8)
    for i in range(1, laplacian.shape[0] - 1):
        for j in range(1, laplacian.shape[1] - 1):
            if laplacian[i, j] > 0:
                if laplacian[i, j] >= laplacian[i - 1, j] and \
                   laplacian[i, j] >= laplacian[i + 1, j] and \
                   laplacian[i, j] >= laplacian[i, j - 1] and \
                   laplacian[i, j] >= laplacian[i, j + 1]:
                    suppressed[i, j] = 255
            else:
                if laplacian[i, j] <= laplacian[i - 1, j] and \
                   laplacian[i, j] <= laplacian[i + 1, j] and \
                   laplacian[i, j] <= laplacian[i, j - 1] and \
                   laplacian[i, j] <= laplacian[i, j + 1]:
                    suppressed[i, j] = 0

    # Apply threshold to get binary edge map
    _, binary = cv2.threshold(suppressed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary

# Read image and convert to grayscale
image = cv2.imread("lena.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform edge detection
edges = log_edge_detection(gray)

# Display the input image and the edge map
fig, axs = plt.subplots(1, 2, figsize=(10, 10))
axs[0].imshow(gray, cmap='gray')
axs[0].set_title("Input Image")
axs[1].imshow(edges, cmap='gray')
axs[1].set_title("Edge Map")
plt.show()