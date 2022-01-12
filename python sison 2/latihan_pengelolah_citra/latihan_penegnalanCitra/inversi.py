import cv2
import os
import numpy as np
os.chdir('C:/Users/Dzaky Faihalariq Pir/Downloads/pythonseson2/latihan_pengelolah_citra/img')


def inversi(nama):
    data = cv2.imread(nama, cv2.IMREAD_GRAYSCALE)
    jmlbaris = data.shape[0]
    jmlkolom = data.shape[1]
    hasil = np.zeros((jmlbaris, jmlkolom), np.uint8)
    for brs in range(jmlbaris):
        for klm in range(jmlkolom):
            hasil[brs, klm] = 225 - data[brs, klm]  # rumus inversi
    cv2.imshow('gambar asli', data)
    cv2.imshow('gambar inversi', hasil)
    cv2.waitKey(0)


nama = os.listdir()
inversi(nama[0])
