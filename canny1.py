import cv2
import numpy as np

def gaussian_smoothing(image, kernel_size=5, sigma=1.4):
    if image is None:
        raise ValueError("Invalid image. Unable to perform Gaussian smoothing.")
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

def compute_gradients(image):
    # Sobel filters for gradient calculation
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    # Compute gradient magnitude and direction
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    gradient_direction = np.arctan2(sobel_y, sobel_x)
    return gradient_magnitude, gradient_direction

def non_maximum_suppression(gradient_magnitude, gradient_direction):
    rows, cols = gradient_magnitude.shape
    suppressed = np.zeros_like(gradient_magnitude)
    angle = gradient_direction * (180.0 / np.pi)
    angle[angle < 0] += 180

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            q = 255
            r = 255
            # Angle quantization
            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                q = gradient_magnitude[i, j+1]
                r = gradient_magnitude[i, j-1]
            elif 22.5 <= angle[i, j] < 67.5:
                q = gradient_magnitude[i+1, j-1]
                r = gradient_magnitude[i-1, j+1]
            elif 67.5 <= angle[i, j] < 112.5:
                q = gradient_magnitude[i+1, j]
                r = gradient_magnitude[i-1, j]
            elif 112.5 <= angle[i, j] < 157.5:
                q = gradient_magnitude[i-1, j-1]
                r = gradient_magnitude[i+1, j+1]
            if (gradient_magnitude[i, j] >= q) and (gradient_magnitude[i, j] >= r):
                suppressed[i, j] = gradient_magnitude[i, j]
    return suppressed

def hysteresis_thresholding(image, low_threshold_ratio=0.05, high_threshold_ratio=0.09):
    high_threshold = np.max(image) * high_threshold_ratio
    low_threshold = high_threshold * low_threshold_ratio

    strong_edges = (image > high_threshold)
    weak_edges = (image >= low_threshold) & (image <= high_threshold)

    rows, cols = image.shape
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if weak_edges[i, j]:
                if strong_edges[i-1:i+2, j-1:j+2].any():
                    strong_edges[i, j] = True
                    weak_edges[i, j] = False
                else:
                    weak_edges[i, j] = False

    return strong_edges.astype(np.uint8) * 255

def canny_edge_detection(image_path, kernel_size=5, sigma=1.4, low_threshold_ratio=0.05, high_threshold_ratio=0.09):
    # Read the input image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Unable to read the image. Please check the file path and image format.")

    # Apply Gaussian smoothing
    smoothed_image = gaussian_smoothing(image, kernel_size, sigma)

    # Compute gradients
    gradient_magnitude, gradient_direction = compute_gradients(smoothed_image)

    # Non-maximum suppression
    suppressed_image = non_maximum_suppression(gradient_magnitude, gradient_direction)

    # Hysteresis thresholding
    canny_edges = hysteresis_thresholding(suppressed_image, low_threshold_ratio, high_threshold_ratio)

    return canny_edges

# Example usage
try:
    canny_edges = canny_edge_detection('lena.jpeg')
    cv2.imshow('Canny Edges', canny_edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print("An error occurred:", e)
