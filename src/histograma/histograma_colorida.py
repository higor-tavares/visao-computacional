# Histograma de uma imagem colorida
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
image = cv2.imread('../../out/fruta-colorida.bmp')
blue,green,red = cv2.split(image)
plt.hist(red.ravel(),256,[0,256])
plt.title('RED')
plt.figure()
plt.hist(green.ravel(),256,[0,256])
plt.title('GREEN')
plt.figure()
plt.hist(blue.ravel(),256,[0,256])
plt.title('BLUE')
plt.show()