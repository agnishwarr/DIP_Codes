import numpy as np
import cv2
def adaptive_median_filter(image, max_window_size=7):
    rows, cols = image.shape
    filtered_image = np.zeros_like(image)
    for i in range(rows):
        for j in range(cols):
            window_size = 3
            while window_size <= max_window_size:
                window = image[max(0, i - window_size//2):min(rows, i + window_size//2 + 1),
                               max(0, j - window_size//2):min(cols, j + window_size//2 + 1)]
                z_min = np.min(window)
                z_max = np.max(window)
                z_med = np.median(window)
                z_xy = image[i, j]
                if z_med > z_min and z_med < z_max:
                    if z_xy > z_min and z_xy < z_max:
                        filtered_image[i, j] = z_xy
                    else:
                        filtered_image[i, j] = z_med
                    break
                else:
                    window_size += 2
    return filtered_image
image = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
filtered_image = adaptive_median_filter(image)
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
