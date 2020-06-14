# Rotate an image 90 °
import cv2 
import numpy as np 
img_path = '../../img/folha.jpg'
original_image = cv2.imread(img_path,0)
rows,cols = original_image.shape
matriz = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
rotated_image = cv2.warpAffine(original_image,matriz,(cols,rows))
cv2.imshow('Imagem rotacionada',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()