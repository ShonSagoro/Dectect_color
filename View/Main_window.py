import cv2
import numpy as np


class MainWindow():
    umbral_bajo = np.array([0, 100, 100])
    umbral_alto = np.array([10, 255, 255])
    img = cv2.imread('public/color_primary.jpg')

    def __init__(self):
        self.img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.mask = cv2.inRange(self.img_hsv, self.umbral_bajo, self.umbral_alto)
        self.res = cv2.bitwise_and(self.img, self.img, mask=self.mask)
        cv2.imshow('Imagen Original vs Detección de Rojo', np.hstack([self.img, self.res]))
        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()