import cv2
original = cv2.imread('../../img/ruido-interno.bmp',0)
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fake = cv2.morphologyEx(original,cv2.MORPH_CLOSE,elemento_estruturante)
cv2.imshow('Original',original)
cv2.imshow('Fake news',fake)
cv2.waitKey(0)
cv2.destroyAllWindows()