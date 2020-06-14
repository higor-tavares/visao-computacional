import cv2
img_path = '../../img/casa.jpg'
origem = cv2.imread(img_path)
img = cv2.GaussianBlur(origem,(3,3),0)
cv2.imshow('Original',origem)
cv2.imshow('Tratada',img)
cv2.waitKey(0)
cv2.destroyAllWindows()