# Mostra uma imagem RGB segmentada para os três canais
# @author Higor Tavares
import cv2
import numpy as np
#caminho 
image_path = '../../dadosImagem/Treinamento/positivos/crop_000010.png'
image = cv2.imread(image_path)
blue,green,red = cv2.split(image)
cv2.imshow("Canal R",red)
cv2.imshow("Canal G",green)
cv2.imshow("Canal B",blue)
cv2.imshow("Imagem original",image)
cv2.imwrite("../../out/person-red.jpeg",red)
cv2.imwrite("../../out/person-green.jpeg",green)
cv2.imwrite("../../out/person-blue.jpeg",blue)
cv2.waitKey(0)
cv2.destroyAllWindows()