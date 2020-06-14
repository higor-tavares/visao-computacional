# Mergia os 3 canais, pra gerar uma imagem RGB
import cv2
red = cv2.imread('../../out/person-red.jpeg',0)
green = cv2.imread('../../out/person-green.jpeg',0)
blue = cv2.imread('../../out/person-blue.jpeg',0)
image = cv2.merge((blue,green,red))
print(image.shape)
cv2.imshow('Person',image)
cv2.imwrite('../../out/person-rgb.jpeg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()