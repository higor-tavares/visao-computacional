import cv2
import numpy as np 
img = cv2.imread('../../img/quadrado.bmp',0)
# Segmentação por binarização
ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
contorno, hierarquia = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# Objetndo contornos do  objeto segmentado
objeto = contorno[0]
moments = cv2.moments(objeto)
cx = int(moments['m10']/moments['m00'])
cy = int(moments['m01']/moments['m00'])
print(cx,cy)