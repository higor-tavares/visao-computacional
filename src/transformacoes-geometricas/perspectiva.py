import cv2
import numpy as np 
img_path = '../../img/sudoku.jpg'
img = cv2.imread(img_path)
origin = np.float32([[190,86],[460,86],[193,373],[485,373]])
destity = np.float32([[0,0],[500,0],[0,500],[500,500]])
transformation = cv2.getPerspectiveTransform(origin,destity)
imgTransf = cv2.warpPerspective(img,transformation,(500,500))
cv2.imshow('Imagem original',img)
cv2.imshow('Imagem transformada',imgTransf)
cv2.waitKey(0)
cv2.destroyAllWindows()