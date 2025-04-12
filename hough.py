import cv2
import numpy as np
import math

def hough_transform(image, threshold):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection using Canny
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Initialize accumulator array
    height, width = edges.shape
    diagonal_length = int(math.sqrt(height ** 2 + width ** 2))
    accumulator = np.zeros((diagonal_length * 2, 180), dtype=np.uint8)

    # Detect edges and populate accumulator array
    for y in range(height):
        for x in range(width):
            if edges[y][x] > 0:
                for theta in range(0, 180):
                    rho = int(x * np.cos(np.deg2rad(theta)) + y * np.sin(np.deg2rad(theta)))
                    accumulator[rho + diagonal_length][theta] += 1

    # Find peaks in the accumulator array
    lines = []
    for rho in range(diagonal_length * 2):
        for theta in range(180):
            if accumulator[rho][theta] > threshold:
                lines.append((rho - diagonal_length, theta))

    # Draw detected lines on the original image
    for rho, theta in lines:
        a = np.cos(np.deg2rad(theta))
        b = np.sin(np.deg2rad(theta))
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return image

# Read the input image
image = cv2.imread("lena.jpeg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Set the threshold for Hough Transform
    threshold = 100

    # Apply Hough Transform
    result_image = hough_transform(image, threshold)

    # Display the result
    cv2.imshow("Hough Transform Result", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
