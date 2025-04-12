import cv2
import numpy as np

def adaptive_median_filter(img, max_size):
    result = np.zeros_like(img)
    padded_img = np.pad(img, max_size, mode='reflect')

    for i in range(max_size, img.shape[0] + max_size):
        for j in range(max_size, img.shape[1] + max_size):
            window_size = 3  # Initial window size
            while window_size <= max_size:
                window = padded_img[i - window_size//2:i + window_size//2 + 1, j - window_size//2:j + window_size//2 + 1]
                window_flat = window.flatten()
                window_flat.sort()

                median = window_flat[window_size * window_size // 2]
                z_min = np.min(window_flat)
                z_max = np.max(window_flat)
                z_med = padded_img[i, j]

                if z_min < z_med < z_max:
                    if z_min < median < z_max:
                        result[i - max_size, j - max_size] = median
                    else:
                        result[i - max_size, j - max_size] = z_med
                    break
                else:
                    window_size += 2

    return result

# Load an image
image = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)

img = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
# Create a mask for salt noise (white pixels)
salt_mask = np.random.choice([True, False], size=img.shape, p=[0.25, 0.75])
# Create a mask for pepper noise (black pixels)
pepper_mask = np.random.choice([True, False], size=img.shape, p=[0.25, 0.75])
# Add salt noise (white pixels)
img[salt_mask] = 255
# Add pepper noise (black pixels)
img[pepper_mask] = 0

# Define parameters
max_size = 7  # Maximum filter size

# Apply the adaptive median filter
filtered_image = adaptive_median_filter(img, max_size)

# Display the original, noisy, and filtered images
cv2.imwrite('AdaptiveMedianFilter_Original_Image.png', image)
cv2.imwrite('AdaptiveMedianFilter_Noisy_Image.png', img)
cv2.imwrite('AdaptiveMedianFilter_Filtered_Image.png', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()