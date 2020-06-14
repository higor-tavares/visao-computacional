import cv2
p1_path = '../../img/posicao_1.bmp'
p2_path = '../../img/posicao_2.bmp'
p1 = cv2.imread(p1_path)
p2 = cv2.imread(p2_path)
img = cv2.subtract(p2,p1)
cv2.imshow('Imagem subtraida',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
