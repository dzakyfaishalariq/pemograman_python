from random import randint,choices
import os
import numpy as np
os.system('cls')
class permainan:
    nilai = []
    poin_pemain = 0
    poin_Komputer = 0
    def __init__(self,nama_pemain,nama_komputer):
        self.nama_pemain = nama_pemain
        self.nama_komputer = nama_komputer
    def pemain(self,angka):
        self.nilai.append(angka)
    def komputer(self):
        komputer = randint(0,20)
        return komputer

mulai = permainan('Dzaky','Asus')
ulang = 'y'
print("Masukan nilai untuk melawan musuh! ")
while ulang == 'y':
    isi = int(input())
    mulai.pemain(isi)
    ulang = input('isi lagi ? [y/t] : ')
for i in range(np.size(mulai.nilai)):
    pilihanKomputer = mulai.komputer()
    if mulai.nilai[i] == pilihanKomputer:
        mulai.poin_pemain += 10
        print("Anda menang dapat sama nilainya dengan komputer anda : {} dan komputer : {}".format(mulai.nilai[i],pilihanKomputer))
    else:    
        mulai.poin_Komputer += 10
        print("anda kalah karena nilai berbeda dengan komputer anda : {} dan komputer : {}".format(mulai.nilai[i],pilihanKomputer))
print("==========Keterangan===========")
print("poin anda : {}".format(mulai.poin_pemain))
print("poin musuh: {}".format(mulai.poin_Komputer))
