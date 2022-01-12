import cv2
import sys
import os

from cv2 import data
os.system('cls')
os.chdir('C:/Users/Dzaky Faihalariq Pir/Downloads/pythonseson2/latihan_pengelolah_citra/img')
data = os.listdir()
print(data)
gambar = cv2.imread(data[1])
gambar1 = gambar[70:300]
#gambar2 = gambar[..., 200:]
iris = gambar[190:280, 170:400]  # irisan yang diambil
# mengubah yang diris menjadi warna biru
# gambar[190:280, 170:400] = [255, 0, 0] mengubah warna pada irisan
cv2.imshow('gambar awal', gambar)
cv2.imshow('gambar irirsan', iris)
cv2.imshow('gambar iris 3', gambar1)
#cv2.imshow('gambar iris 4', gambar2)
cv2.waitKey(0)
cv2.destroyAllWindows()
