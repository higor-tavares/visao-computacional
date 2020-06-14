# A sample program to identify and classify an image 
# Author <Higor Tavares>
import cv2 
# Classificadores
catClassifier = cv2.CascadeClassifier('../../data/cat2.xml')
# Imagem original
img = cv2.imread('../../img/mutigatos9.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Verificando se é um gato
cats = catClassifier.detectMultiScale(gray,1.3,1,20)
for (x,y,w,h) in cats:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# resize image
resized = cv2.resize(img, (600,450), interpolation = cv2.INTER_AREA)
mensagem = 'Conta-gatos: Encontrei '+str(len(cats))+' gatos na imagem'
cv2.imshow(mensagem,resized)
cv2.waitKey(0)
cv2.destroyAllWindows()