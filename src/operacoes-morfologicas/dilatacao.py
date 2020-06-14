import cv2
import numpy as np 
img_path = '../../img/rolamento.bmp'
original = cv2.imread(img_path,0)
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
processada = cv2.dilate(original,elemento_estruturante,iterations=2)
cv2.imshow('Original',original)
cv2.imshow('Processada',processada)
cv2.waitKey(0)
cv2.destroyAllWindows()