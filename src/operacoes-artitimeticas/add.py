import cv2
red_path = '../../img/fichas-vermelhas.bmp'
black_path = '../../img/fichas-pretas.bmp'
img_red = cv2.imread(red_path)
img_black = cv2.imread(black_path)
img = cv2.add(img_red,img_black)
cv2.imshow('Soma',img)
cv2.waitKey(0)
cv2.destroyAllWindows()