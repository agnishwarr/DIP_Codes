import cv2
import numpy as np

def label_components(image):
    num_labels, labels = cv2.connectedComponents(image)
    # Add 1 to labels to avoid conflicts with background (label 0)
    labels = labels + 1
    # Map background to 0
    labels[image == 0] = 0
    return num_labels, labels

# Define the dimensions of the image
width = 200
height = 200

# Create a numpy array of zeros with the defined dimensions
binary_image = np.zeros((height, width), dtype=np.uint8)

# Draw a white square in the middle of the image
square_size = 50
start_x = (width - square_size) // 2
start_y = (height - square_size) // 2
end_x = start_x + square_size
end_y = start_y + square_size
binary_image[start_y:end_y, start_x:end_x] = 1

# Apply component labeling
num_labels, labeled_image = label_components(binary_image)

# Display the labeled image
cv2.imshow('Labeled Image', (labeled_image * 255).astype(np.uint8))  # Multiply by 255 to display as white (255) and black (0)
cv2.waitKey(0)
cv2.destroyAllWindows()
