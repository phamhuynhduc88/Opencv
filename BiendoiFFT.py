import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('F://hoa.jpg',0)
f = np.fft.fft2(img)  #Fourier transform to get the frequency spectrum, generally speaking, the low-frequency component has the largest modulus
fshift = np.fft.fftshift(f)#Shift the spectrum to the center of the image
# Convert spectrum to db
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(321),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])


rows, cols = img.shape
crow,ccol = rows//2 , cols//2
#Design a high pass filter corresponding to 0, low frequency corresponds to 1
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
#Translation inverse transformation
f_ishift = np.fft.ifftshift(fshift)
#Fourier inverse transform
img_back = np.fft.ifft2(f_ishift)
# Take the absolute value
img_back = np.abs(img_back)
plt.subplot(323),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()
