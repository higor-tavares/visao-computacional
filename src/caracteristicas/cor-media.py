import cv2
rgb = cv2.imread('../../img/tampa.jpg')
gray = cv2.imread('../../img/tampa-tons-de-cinza.jpg',0)
media_rgb = cv2.mean(rgb)
media_gray = cv2.mean(gray)
print(media_rgb)
print(media_gray)