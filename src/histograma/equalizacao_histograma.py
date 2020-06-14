# Equalização de histograma para aumentar o contraste e a nitidez
# @author Higor Tavares
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
img_path = '../../img/relogio.bmp'
original_image = cv2.imread(img_path,0)
equilized_image = cv2.equalizeHist(original_image)
cv2.imshow('Imagem original',original_image)
cv2.imshow('Imagem equilizada',equilized_image)
plt.hist(original_image.ravel(),256,[0,256])
plt.title('Imagem original')
plt.figure()
plt.hist(equilized_image.ravel(),256,[0,256])
plt.title('Imagem equalizada')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()