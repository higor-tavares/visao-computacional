# Gradiente Morfológico
# Operação entre a erosão e a dilatação de uma imagem
# author: Higor Tavares
import cv2
img_path = '../../img/rolamento.bmp'
# Carrega a imagem
img = cv2.imread(img_path,0)
# Elemento estruturante (Matriz)
structure_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
# Aplica a operação de gradiente morfologico a imagem
processed_img = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,structure_element)
# Exibe os resultados
cv2.imshow('Original',img)
cv2.imshow('Grandiente Morfologico',processed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
