import cv2
import numpy as np
import os
os.system('cls')
os.chdir('C:/Users/Dzaky Faihalariq Pir/Downloads/pythonseson2/latihan_pengelolah_citra/img')
data = os.listdir()


def fungsi(nama, ambang):
    citra = cv2.imread(nama, cv2.IMREAD_GRAYSCALE)
    jmlbaris = citra.shape[0]
    jmlcolom = citra.shape[1]
    hasil = np.zeros((jmlbaris, jmlcolom), np.uint8)
    for brs in range(jmlbaris):
        for klm in range(jmlcolom):
            if citra[brs, klm] >= ambang:
                hasil[brs, klm] = 255
    cv2.imshow('Asli', citra)
    cv2.imshow('Biner', hasil)
    cv2.waitKey(0)
    return nama, ambang


nama, ambang = fungsi(data[0], 150)
print("nama file : {}".format(nama))
print("nilai ambang : {}".format(ambang))
