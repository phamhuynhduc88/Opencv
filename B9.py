import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('F://hoa.jpg',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO']
images = [img, thresh1, thresh2, thresh3, thresh4]
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
