import cv2
import numpy as np
def adaptive_mean_filter(image, window_size, noise_stddev):  
    height, width = image.shape[:2]
    output_image = np.zeros((height, width), dtype=np.uint8)
    half_window = window_size // 2
    for i in range(half_window, height - half_window):
        for j in range(half_window, width - half_window):
            window = image[i - half_window:i + half_window + 1, j - half_window:j + half_window + 1]
            local_mean = np.mean(window)
            local_stddev = np.std(window)
            filtered_pixel = image[i][j]
            if local_stddev != 0:
                filtered_pixel = image[i, j] - ((noise_stddev / local_stddev) * (image[i, j] - local_mean))
            output_image[i, j] = np.clip(filtered_pixel, 0, 255)
    return output_image
src_image = cv2.imread('lena.jpeg', cv2.IMREAD_GRAYSCALE)
mean = 0
stddev = 50
noise = np.zeros(src_image.shape, np.uint8)
cv2.randn(noise, mean, stddev)
input_image = cv2.add(src_image, noise)
window_size = 7 # Adjust as needed
noise_stddev = 20 # Adjust as needed
output_image = adaptive_mean_filter(input_image, window_size, noise_stddev)
cv2.imwrite('Adaptive_Input_Image.png', src_image)
cv2.imwrite('Adaptive_Noise_on_Input_Image.png', input_image)
cv2.imwrite('Adaptive_Filtered_Image.png', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()