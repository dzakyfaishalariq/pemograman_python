import cv2
import numpy as np


class pengolahanCitra:

    def __init__(self, nama):
        self.__nama = nama
    # pengaturan kecerahan

    def negatif(self):
        citra = cv2.imread(self.__nama)
        cv2.imshow('Citra Hasil', citra)
        hasil = 255 - citra
        hasil2 = citra + 50
        cv2.imshow("Citra hasil 2", hasil)
        cv2.imshow("Citra hasil 3", hasil2)
        cv2.waitKey(0)
