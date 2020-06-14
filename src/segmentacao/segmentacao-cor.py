# Segmentação por cor
# Utiliza cores do espaço HSV
# autor: Higor Tavares
import cv2
import numpy as np 
rgb_img = cv2.imread('../../img/pesadown.jpg')
hsv_img = cv2.cvtColor(rgb_img,cv2.COLOR_BGR2HSV)
low_red = np.array([160,100,100])
high_red = np.array([200,255,255])
low_green = np.array([31, 52, 72])
high_green = np.array([102, 255, 255])
low_yellow = np.array([20,100,100])
high_yellow = np.array([30,255,255])
red_image = cv2.inRange(hsv_img,low_red,high_red)
yellow_image = cv2.inRange(hsv_img,low_yellow,high_yellow)
green_image = cv2.inRange(hsv_img,low_green,high_green)
aux = cv2.add(red_image,green_image)
total = cv2.add(aux,yellow_image)
cv2.imshow('Original',rgb_img)
cv2.imshow('Vermelho',red_image)
cv2.imshow('Verde',green_image)
cv2.imshow('Amarelo',yellow_image)
cv2.imshow('Todas',total)
cv2.waitKey(0)
cv2.destroyAllWindows()