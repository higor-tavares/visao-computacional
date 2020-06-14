import cv2
original = cv2.imread('../../img/arroz.bmp',0)
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_CROSS,(100,100))
processada = cv2.morphologyEx(original,cv2.MORPH_OPEN,elemento_estruturante)
subtraida = cv2.subtract(original,processada)
#tratada
tratada = cv2.add(subtraida,subtraida)
cv2.imshow('Original',original)
cv2.imshow('Processada',processada)
cv2.imshow('Subtraida',subtraida)
cv2.imshow('Tratada',tratada)
cv2.waitKey(0)
cv2.destroyAllWindows()
