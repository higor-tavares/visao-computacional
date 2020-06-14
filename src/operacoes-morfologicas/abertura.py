import cv2
original = cv2.imread('../../img/rolamento-ruido.bmp',0)
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
processada = cv2.morphologyEx(original,cv2.MORPH_OPEN,elemento_estruturante)
cv2.imshow('Original',original)
cv2.imshow('Processada',processada)
cv2.waitKey(0)
cv2.destroyAllWindows()