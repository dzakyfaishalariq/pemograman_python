import cv2
import os
os.system('cls')
# mencari lokasi untuk membukak hasil kerja
os.chdir('C:/Users/Dzaky Faihalariq Pir/Downloads/pythonseson2/latihan_pengelolah_citra/img')
# menampilkan hasil pencarian
# print(os.getcwd())
# isi berkas yang ada di dalam folder
data = os.listdir()
citra_RGB = cv2.imread(data[0])
citra_ABU_ABU = cv2.cvtColor(citra_RGB, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gambar Berwarna', citra_RGB)
cv2.imshow('Gambar Abu - Abu', citra_ABU_ABU)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('selesai')