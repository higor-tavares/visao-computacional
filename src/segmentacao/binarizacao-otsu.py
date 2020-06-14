# Segmentação por binárização
# O limiar é definido pelo algoritimo otsu 
# com base no histograma da imagem apresentando 
# qum melhor resultado do que o obtido por tentativa e erro
# Author: Higor Tavares
import cv2
path = '../../img/graos-cafe.bmp'
# Carrega a imagem em tons de cinza
img = cv2.imread(path,0)
tipo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
ret, binary = cv2.threshold(img,0,255,tipo)
print(tipo)
cv2.imshow('Original',img)
cv2.imshow('Binarizada',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()