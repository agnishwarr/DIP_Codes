import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the source image
source_image = cv2.imread('lena.jpeg')

# Add Gaussian noise to a copy of the source image
gaussian_noise = np.random.normal(0, 25, source_image.shape).astype(np.uint8)
noisy_image_gaussian = cv2.add(source_image, gaussian_noise)

# Add salt-and-pepper noise to another copy of the source image
salt_prob = 0.02
pepper_prob = 0.02
salt_pepper_noise = np.random.choice([0, 255], size=source_image.shape[:2], p=[salt_prob, pepper_prob])
noisy_image_salt_pepper = cv2.add(source_image, salt_pepper_noise)

# Add speckle noise to yet another copy of the source image
speckle_noise = np.random.randn(*source_image.shape).astype(np.uint8) * 50
noisy_image_speckle = cv2.add(source_image, speckle_noise)

# Define the scale parameter for exponential noise
scale = 0.05

# Add exponential noise to another copy of the source image
exponential_noise = np.random.exponential(scale, source_image.shape).astype(np.uint8)
noisy_image_exponential = cv2.add(source_image, exponential_noise)

# Add Poisson noise to another copy of the source image
poisson_noise = np.random.poisson(50, source_image.shape).astype(np.uint8)
noisy_image_poisson = cv2.add(source_image, poisson_noise)

# Add uniform noise to another copy of the source image
uniform_noise = np.random.uniform(-50, 50, source_image.shape).astype(np.uint8)
noisy_image_uniform = cv2.add(source_image, uniform_noise)

# Add Laplacian noise to another copy of the source image
laplacian_noise = np.random.laplace(0, 25, source_image.shape).astype(np.uint8)
noisy_image_laplacian = cv2.add(source_image, laplacian_noise)

# Plot the images
noisy_images = [
    noisy_image_gaussian,
    noisy_image_salt_pepper,
    noisy_image_speckle,
    noisy_image_exponential,
    noisy_image_poisson,
    noisy_image_uniform,
    noisy_image_laplacian
]

titles = [
    'Gaussian Noise',
    'Salt and Pepper Noise',
    'Speckle Noise',
    'Exponential Noise',
    'Poisson Noise',
    'Uniform Noise',
    'Laplacian Noise'
]

plt.figure(figsize=(15, 10))
for i in range(len(noisy_images)):
    plt.subplot(2, 4, i + 1)
    plt.imshow(cv2.cvtColor(noisy_images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
