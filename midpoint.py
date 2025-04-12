import cv2
import numpy as np

def add_gaussian_noise(image, std):
    """
    Adds Gaussian noise to an image.

    Args:
        image: NumPy array representing the image.
        std: Standard deviation of the Gaussian noise.

    Returns:
        A new NumPy array with Gaussian noise added.
    """
    row, col, ch = image.shape
    # Generate Gaussian noise with mean 0 and specified std
    noise = np.random.normal(0, std, (row, col, ch)).astype(np.float32)
    # Add noise to the image
    noisy_image = image + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)  # Clip to [0, 255] range

def midpoint_filter(image, window_size):
    """
    Applies a midpoint filter to remove noise from an image.

    Args:
        image: NumPy array representing the noisy image.
        window_size: Size of the filter window (e.g., 3, 5).

    Returns:
        A new NumPy array with noise reduced using the midpoint filter.
    """
    pad_width = window_size // 2
    padded_image = cv2.copyMakeBorder(image, pad_width, pad_width, pad_width, pad_width, cv2.BORDER_REPLICATE)
    row, col, ch = image.shape
    filtered_image = np.zeros_like(image)

    for i in range(pad_width, row + pad_width):
        for j in range(pad_width, col + pad_width):
            window = padded_image[i-pad_width:i+pad_width+1, j-pad_width:j+pad_width+1, :]
            # Find minimum and maximum intensity values
            min_val, max_val = np.min(window), np.max(window)
            # Calculate midpoint
            midpoint = (min_val + max_val) // 2
            filtered_image[i - pad_width, j - pad_width] = midpoint.astype(np.uint8)

    return filtered_image

# Load your image
image = cv2.imread("lena.jpeg")

# Add Gaussian noise with standard deviation 10 (reduced from 100)
noisy_image = add_gaussian_noise(image.copy(), 10)  # Decreased standard deviation

# Apply midpoint filter with larger window size, e.g., 5
filtered_image = midpoint_filter(noisy_image, 5)  # Increased window size

# Display original, noisy, and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
