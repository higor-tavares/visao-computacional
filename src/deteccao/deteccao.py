import cv2 
import numpy as np 
# Arquivo com as caracteristicas
cascadeFace = cv2.CascadeClassifier('../../data/haarcascade_frontalface_default.xml')
# Imagem original 
img = cv2.imread('../../img/selecao.png')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = cascadeFace.detectMultiScale(img_gray,1.3,5,30)
# Desenha um retangulo nas faces detectadas
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# resize image
resized = cv2.resize(img, (600,450), interpolation = cv2.INTER_AREA)
# Exibe o numero de faces
print('Existem '+str(len(faces))+' Pessoas na imagem')
cv2.imshow('Resutado',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()