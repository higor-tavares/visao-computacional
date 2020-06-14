# Programa que exibe uma imagem
# @author Higor Tavares
import cv2
#caminho 
image_path = '../../dadosImagem/Treinamento/positivos/crop_000010.png'
image = cv2.imread(image_path)
#exibe a imagem
cv2.imshow('Pessoa',image)
cv2.waitKey(0)
cv2.destroyAllWindows()