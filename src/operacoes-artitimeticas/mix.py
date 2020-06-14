import cv2
red_path = '../../img/fichas-vermelhas.bmp'
black_path = '../../img/fichas-pretas.bmp'
img_red = cv2.imread(red_path)
img_black = cv2.imread(black_path)
img = cv2.addWeighted(img_black,0.2,img_red,1.0,0)
cv2.imshow('Mix',img)
cv2.waitKey(0)
cv2.destroyAllWindows()