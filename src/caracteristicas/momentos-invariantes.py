import cv2 
import numpy as np 
img = cv2.imread('../../img/engrenagem-1.bmp',0)
moments = cv2.moments(img)
hu_moments = cv2.HuMoments(moments)
# Aplicando trasnformação logaritmica
print('Imagem 1\n')
print(-np.sign(hu_moments)*np.log10(np.abs(hu_moments)))
img = cv2.imread('../../img/engrenagem-2.bmp',0)
moments = cv2.moments(img)
hu_moments = cv2.HuMoments(moments)
# Aplicando trasnformação logaritmica
print('Imagem 2\n')
print(-np.sign(hu_moments)*np.log10(np.abs(hu_moments)))
img = cv2.imread('../../img/engrenagem-3.bmp',0)
moments = cv2.moments(img)
hu_moments = cv2.HuMoments(moments)
# Aplicando trasnformação logaritmica
print('Imagem 3\n')
print(-np.sign(hu_moments)*np.log10(np.abs(hu_moments)))