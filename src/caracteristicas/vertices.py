import cv2
rgb = cv2.imread('../../img/quadrado.bmp')
gray = cv2.imread('../../img/quadrado.bmp',0)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contornos,hierarquia = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
objeto = contornos[0]
# Obtendo o perimetro 
perimetro = cv2.arcLength(objeto,True)
# Obtendo vertices
poligono = cv2.approxPolyDP(objeto,perimetro*0.1,True)
# Obtendo número de vertices
totalVertices =  len(poligono)
print(totalVertices)