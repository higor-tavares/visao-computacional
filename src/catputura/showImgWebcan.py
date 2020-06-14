# Captura imagens da webcan e exibe na tela
# @author Higor Tavares
import cv2
captura = cv2.VideoCapture(0)
while True:
    ret,frame = captura.read()
    cv2.imshow('Webcan',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
captura.release()
cv2.destroyAllWindows()