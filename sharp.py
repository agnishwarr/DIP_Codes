import cv2
import numpy
# import numpy as np
#
img = cv2.imread("lena.jpeg", 0)
# # img = np.array([[2, 3], [4, 5]])
# img2 = np.pad(img, (1, 1), mode="constant")
# img2 = img2[1:img.shape[0] + 1, 2:]
#
# gx = img2 - img
#
# img_padded = np.pad(img, ((1, 0), (1, 0)), mode="constant")
# # Slice the padded image to calculate gy
# gy = img_padded[:-1, 1:] - img
# # gy = img.transpose() - img2.transpose()
#
#
# #
# # # for i in range(img.shape[0] - 1):
# # #     for j in range(img.shape[1]):
# # #         gx[i][j] = img[i + 1][j] - img[i][j]
# # #
# # # img = img.transpose()
# # # for i in range(img.shape[0] - 1):
# # #     for j in range(img.shape[1]):
# # #         gy[i][j] = img[i + 1][j] - img[i][j]
# #
# # gy = gy.transpose()



import numpy as np


def calculate_gradients(image):
    height, width = image.shape
    gx = np.zeros_like(image, dtype=np.float32)
    gy = np.zeros_like(image, dtype=np.float32)

    # Calculate gx and gy for each pixel
    for y in range(height):
        for x in range(width):
            if x < width - 1:
                gx[y, x] = image[y, x + 1] - image[y, x]
            if y < height - 1:
                gy[y, x] = image[y + 1, x] - image[y, x]

    return gx, gy


# # Create a sample 2D array representing f(x, y)
# f_xy = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

gx, gy = calculate_gradients(img)

print("gx:")
print(gx)

print("\ngy:")
print(gy)

output = numpy.sqrt(numpy.square(gx))  # + numpy.square(gy))
output = output.astype(np.uint8)
cv2.imshow("Input", img)
cv2.imshow("Sharpening", output)
cv2.waitKey(0)
cv2.destroyAllWindows()