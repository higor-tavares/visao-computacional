# Deslocamento da imagem
import cv2 
import numpy as np 
img_path = '../../img/folha.jpg'
image = cv2.imread(img_path)
rows,columns = image.shape[:2]
matriz = np.float32([[1,0,100],[0,1,100]])
displaced_image = cv2.warpAffine(image,matriz,(columns,rows))
cv2.imshow('Imagem deslocada',displaced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()