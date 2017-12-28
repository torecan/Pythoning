import cv2
import numpy as np
from tkinter import *
from tkinter.filedialog import askopenfilename
import os

import matplotlib.pyplot as plt
p1=False
p2=False
x1=0
x2=0
y1=0
y2=0

def show(e,x,y,flags,param):
   global x1,y1,x2,y2
   global p1,p2
   if (e==cv2.EVENT_MOUSEMOVE):
         print(img[y,x])
   elif (e==cv2.EVENT_LBUTTONUP):
         zoom(x,y)
         p1=True

   elif (e==cv2.EVENT_LBUTTONDOWN):
         yoom(x,y)
         p2=True
   elif (e==cv2.EVENT_LBUTTONDBLCLK):
         p1=False
         p2=False
         cv2.imshow("test",img)
   if (p1==True and p2==True):
      print("burda")
      print("x1:" + str(x1))
      print("x2:" + str(x2))
      print("y1:" + str(y1))
      print("y2:" + str(y2))
      if (x2 >= x1 and y2 >= y2):
         img2=img[x1:x2,y1:y2]
         cv2.imshow("test2",img2)
   
         
def zoom(x,y):
   global x1
   global y1
   global p1
   
   x1=x
   y1=y
   p1=True
   
def yoom(x,y):
   global x2
   global y2
   global p2
   
   x2=x
   y2=y
   p2=True
   


file = askopenfilename()
img=cv2.imread(file)

cv2.imshow("test",img)

cv2.setMouseCallback("test",show)

   

cv2.waitKey()
cv2.destroyAllWindows()
