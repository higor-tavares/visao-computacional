import cv2
import numpy as np 
img_path = '../../img/folha.jpg'
img = cv2.imread(img_path)
resized_img = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Redimencionada',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()