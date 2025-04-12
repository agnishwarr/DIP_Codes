import cv2
import numpy as np
def alpha_trimmed_mean_filter(image, filter_size, alpha):
    output = np.zeros_like(image)
    pad_size = filter_size // 2

    for i in range(pad_size, image.shape[0] - pad_size):
        for j in range(pad_size, image.shape[1] - pad_size):
            neighborhood = image[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1]
            flattened_neighborhood = neighborhood.flatten()
            flattened_neighborhood.sort()
            num_to_exclude = int(alpha * filter_size * filter_size / 2)
            trimmed_neighborhood = flattened_neighborhood[num_to_exclude:-num_to_exclude]
            mean_value = np.mean(trimmed_neighborhood)
            output[i, j] = mean_value
    return output
img = cv2.imread("lena.jpeg", 0)
image = cv2.imread("lena.jpeg", 0)
salt_pepper_noise = np.random.choice([0, 255], size=img.shape, p=[0.9, 0.1]) #10% of the pixel values to 255 (white) and 90% of the pixel values to 0 (black)
salt_pepper_noise = salt_pepper_noise.astype(np.uint8)
img = cv2.add(img, salt_pepper_noise)
salt_pepper_noise = np.zeros_like(img)
salt_indices = np.random.choice(img.size, int(0.1 * img.size), replace=False)
salt_pepper_noise.flat[salt_indices] = 255
pepper_indices = np.random.choice(img.size, int(0.9 * img.size), replace=False)
salt_pepper_noise.flat[pepper_indices] = 0
img = cv2.add(img, salt_pepper_noise)
salt_mask = np.random.choice([True, False], size=img.shape, p=[0.05, 0.95])
pepper_mask = np.random.choice([True, False], size=img.shape, p=[0.05, 0.95])
img[salt_mask] = 255
img[pepper_mask] = 0
filter_size = 5
alpha = 0.3  
out = alpha_trimmed_mean_filter(img, filter_size, alpha)
out = out.astype(np.uint8)
cv2.imwrite("AlphaTrimmered_Input.png", image)
cv2.imwrite("AlphaTrimmered_Noise.png", img)
cv2.imwrite("AlphaTrimmered_Output.png", out)
cv2.waitKey(0)
cv2.destroyAllWindows()