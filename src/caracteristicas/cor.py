import cv2
import statistics
binary = cv2.imread('../../img/tampa-binaria.bmp',0)
gray = cv2.imread('../../img/tampa-tons-de-cinza.jpg',0)
rol_binary = binary.ravel()
rol_gray = gray.ravel()
print(statistics.mode(rol_binary))
print(statistics.mode(rol_gray))