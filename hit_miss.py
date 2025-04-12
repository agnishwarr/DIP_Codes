import numpy as np 
import matplotlib.pyplot as plt 
import cv2
b1=np.array([[0,1,0],
              [1,1,1],
              [0,1,0]])
b2=np.array([[0,0,1,0,0],
             [0,1,1,1,0],
             [1,1,1,1,1],
             [0,1,1,1,0],
             [0,0,1,0,0]])
image=np.array([[0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,1,1,1,1,0,0],
                [0,1,1,1,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,1,1,0,0],
                [0,0,0,0,1,0,0,1,1,1,0],
                [0,0,0,1,1,1,0,0,1,0,0],
                [0,0,0,0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0]])
cnt=1-image
def erode(image,win):
    output=np.zeros_like(image)
    for i in range (win.shape[0]//2,image.shape[0]-win.shape[0]//2):
        for j in range (win.shape[1]//2,image.shape[1]-win.shape[1]//2):
            roi=image[i-win.shape[0]//2:i+win.shape[0]//2+1,j-win.shape[1]//2:j+win.shape[1]//2+1]
            #result=np.min(roi*b1)
            result=np.logical_and(roi,win)
            if np.all(result==win):
                output[i,j]=1
    return output
def dilate (image,win):
    output=np.zeros_like(image)
    for i in range (1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            roi=image[i-1:i+2,j-1:j+2]
            result=np.max(roi*win)
            #result=np.logical_or(roi,win)
            if result==1 or result==255:
                output[i,j]=255
    return output
def handm(first_half,second_half,win):
    intersected_image=np.logical_and(first_half,second_half)
    return dilate(intersected_image,win)
first_half = erode(image, b1)
b2[1:4,1:4]=b2[1:4,1:4]-b1
second_half = erode(1 - image, b2) # Taking complement of the image for second erosion
intersected_image = handm(first_half,second_half,b1)
plt.subplot(3,3,1)
plt.imshow(image,cmap='grey')
plt.title('original_image')
plt.subplot(3,3,2)
plt.imshow(first_half,cmap='grey')
plt.title('eroded_image_fh')
plt.subplot(3,3,3)
plt.imshow(second_half,cmap='grey')
plt.title('eroded_image_sh')
plt.subplot(3,3,4)
plt.imshow(intersected_image,cmap='grey')
plt.title('Intersection')
plt.show()
