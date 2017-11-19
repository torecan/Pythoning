import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread("C://Users//t.celik//Desktop//img3.png",1)
img2= cv2.imread("C://Users//t.celik//Desktop//img3.png",0)
img3= cv2.imread("C://Users//t.celik//Desktop//img3.png",-1)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()

cv2.imshow("img",img)
cv2.imshow("img2",img2)
cv2.imshow("img3",img3)

cv2.waitKey(0)
