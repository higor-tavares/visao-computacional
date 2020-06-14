# Segmenta as imagens dividindo em 3 valores
# HSV - Matiz (hue), Saturação (saturation) e Valor (value)
# @author Higor Tavares
import cv2 
image_path = '../../dadosImagem/Treinamento/positivos/crop_000010.png'
image = cv2.imread(image_path)
image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
matiz,saturacao,valor = cv2.split(image)
cv2.imshow('Matiz',matiz)
cv2.imshow('Saturacao',saturacao)
cv2.imshow('Valor',valor)
#Convertendo de volta
original = cv2.merge((matiz,saturacao,valor))
original = cv2.cvtColor(original,cv2.COLOR_HSV2BGR)
cv2.imshow('Original',original)
cv2.waitKey(0)
cv2.destroyAllWindows()