# Segmentação por binárização adaptativa 
# Aplicada em imagens onde 
# a distribuição de luminosidade não é uniforme
# Author: Higor Tavares
import cv2 
img = cv2.imread('../../img/comprimidos.bmp',0)
# trata o ruído gausiano
processed_img = cv2.medianBlur(img,9)
binary_img = cv2.adaptiveThreshold(processed_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY_INV,11,5)
cv2.imshow('Original',img)
cv2.imshow('Binarizada',binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()