import cv2 
import numpy as np 
rgb = cv2.imread('../../img/puzzle.bmp')
img = cv2.imread('../../img/puzzle.bmp',0)
ret, binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
contornos, hierarquia = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
objeto = contornos[0]
# Obtendo os  vertices do retangulo
(x,y), raio = cv2.minEnclosingCircle(objeto)
#converte para int
centro = (int(x),int(y))
raio = int(raio)
# Desenhando o retangulo na imagem (imagem,vertice p1, vertice oposto, cor BGR, expessura)
cv2.circle(rgb,centro,raio,(0,255,0),2)
cv2.imshow('Circulo envolvente',rgb)
print(x,y,raio)
cv2.waitKey(0)
cv2.destroyAllWindows()