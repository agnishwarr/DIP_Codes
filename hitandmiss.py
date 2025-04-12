import numpy as np
import matplotlib.pyplot as plt

def hit_miss_transform(image, struct_element):
    padded_image = np.pad(image, ((1, 1), (1, 1)), mode='constant') 

    result = np.zeros_like(image)
    rows, cols = image.shape

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            template = padded_image[i-1:i+2, j-1:j+2]
            center = template[1, 1]
            template[1, 1] = 0  
            if np.all(np.logical_or(template == 0, (struct_element == 1) & (template == center))):
                result[i-1, j-1] = 1

    return result.astype(bool)

regions = np.zeros((10, 10), dtype=bool) 
regions[1, :2] = 1
regions[5:8, 6: 8] = 1
regions[8, 0] = 1


struct_element = np.array([[0, 1, 0],
                            [1, 1, 1],
                            [0, 1, 0]])

plt.figure(figsize=(15, 5))


plt.subplot(1, 3, 1)
plt.imshow(regions, cmap='binary') 
plt.title("Original Binary Image")


plt.subplot(1, 3, 2)
plt.imshow(struct_element, cmap='binary')
plt.title("Structuring Element")


plt.subplot(1, 3, 3)
img = hit_miss_transform(regions, struct_element)
plt.imshow(img, cmap='binary')
plt.title("Image after Hit-Miss Transform")

plt.tight_layout()
plt.show()
