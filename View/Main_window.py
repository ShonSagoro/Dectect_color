import cv2
import numpy as np


class MainWindow():
    umbral_bajo1 = (170, 100, 100)
    umbral_alto1 = (179, 255, 255)
    umbral_bajo2 = (0, 100, 100)
    umbral_alto2 = (10, 255, 255)
    img_original = cv2.imread('public/color_primary.jpg')

    def __init__(self):
        self.img_hsv = cv2.cvtColor(self.img_original, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(self.img_hsv, self.umbral_bajo1, self.umbral_alto1)
        mask2 = cv2.inRange(self.img_hsv, self.umbral_bajo2, self.umbral_alto2)
        self.mask = mask1 + mask2
        self.res = cv2.bitwise_and(self.img_original, self.img_original, mask=self.mask)
        cv2.imshow('Imagen Original vs Detección de Rojo', np.hstack([self.img_original, self.res]))
        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
