# exibe o histograma de uma imagem preta e branca
import cv2
import numpy as np
from matplotlib import pyplot as pyplot
img = cv2.imread('../../img/relogio.bmp',0)
pyplot.hist(img.ravel(),256,[0,256])
pyplot.show()