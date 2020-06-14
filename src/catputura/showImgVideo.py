#exibe imagem de um video mp4
import cv2
import time
captura = cv2.VideoCapture('../../videos/video.mp4')
while True:
    time.sleep(0.02)
    ret, frame = captura.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
captura.release()
cv2.destroyAllWindows()