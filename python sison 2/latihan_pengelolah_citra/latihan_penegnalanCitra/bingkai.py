import cv2
import sys
import os
os.system('cls')
os.chdir(
    'C:/Users/Dzaky Faihalariq Pir/Downloads/pythonseson2/latihan_pengelolah_citra/img')
citra = os.listdir()
citra_conv = cv2.imread(citra[0])
hasil = citra_conv.copy()
# pengolahan citra
Tebal = 30
Hitam = [0, 0, 0]
jmlhBaris = hasil.shape[0]
jmlhKolom = hasil.shape[1]
# pembuatan bingkai
# atas
for baris in range(Tebal):
    for kolom in range(jmlhKolom):
        hasil[baris, kolom] = Hitam
# bawah
for baris in range(jmlhBaris-Tebal-1, jmlhBaris):
    for kolom in range(jmlhKolom):
        hasil[baris, kolom] = Hitam
# Kiri
for baris in range(Tebal, jmlhBaris-Tebal-1):
    for kolom in range(Tebal):
        hasil[baris, kolom] = Hitam
# kanan
for baris in range(Tebal, jmlhBaris-Tebal-1):
    for kolom in range(jmlhKolom-Tebal-1, jmlhKolom):
        hasil[baris, kolom] = Hitam

cv2.imshow('Gambar semula', citra_conv)
cv2.imshow('Gambar hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(hasil.shape)
