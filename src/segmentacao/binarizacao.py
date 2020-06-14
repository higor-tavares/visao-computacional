# Segmentação por binárização
# O limiar é definido por tentativa e erro
# Author: Higor Tavares
import cv2
path = '../../img/engrenagem.jpg'
# Carrega a imagem em tons de cinza
img = cv2.imread(path,0)
ret, binary = cv2.threshold(img,155,255,cv2.THRESH_BINARY_INV)
struture_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# Aplicando operação de abertura para corrigir ruídos internosls
processed = cv2.morphologyEx(binary,cv2.MORPH_CLOSE,struture_element)
cv2.imshow('Original',img)
cv2.imshow('Binarizada',binary)
cv2.imwrite('../../out/binaria.bmp',binary)
cv2.imshow('Tratada',processed)
cv2.waitKey(0)
cv2.destroyAllWindows()