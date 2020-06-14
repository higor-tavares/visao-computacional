import cv2
import numpy as np 
img = cv2.imread('../../img/quadrado.bmp',0)
moments = cv2.moments(img)
print(moments)