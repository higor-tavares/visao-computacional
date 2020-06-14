# converte uma imagem colorida em um bitmap de uma imagem binária
import cv2
img_path = '../../img/fruta.jpeg'
img = cv2.imread(img_path)
img = cv2.resize(img,(300,300))
cv2.imshow('Imagem',img)
cv2.imwrite('../../out/fruta-colorida.bmp',img)
cv2.waitKey(0)
cv2.destroyAllWindows()