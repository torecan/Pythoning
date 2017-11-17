import numpy as np
import cv2

cap = cv2.VideoCapture("C://Users//t.celik//Desktop//write2r.avi")

while True:
 ret, frame = cap.read()

 cv2.imshow("frame",frame)
 cv2.waitKey(33)


