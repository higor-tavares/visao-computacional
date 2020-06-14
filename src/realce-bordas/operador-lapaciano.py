import cv2
original = cv2.imread('../../img/estacionamento.png',0)
img = cv2.Laplacian(original,cv2.CV_8U)
cv2.imshow('Original',original)
cv2.imshow('Lapaciano',img)
cv2.waitKey(0)
cv2.destroyAllWindows()