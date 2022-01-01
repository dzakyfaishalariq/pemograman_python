from colorama import Fore, Style
import os
#algoritma enkripsi
import numpy as np
from numpy.core.fromnumeric import size
os.system('cls')
abjat = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nilai = []
gabungan = {}
for i in range(np.size(abjat)):
    nilai.append(i)
    gabungan[abjat[i]] = i
#melakukan inputan kata kat
print(Fore.GREEN)
print("Masukan kata kata yang ingin dirahasiakan :")
kalimat = input("-> : ")
print("Masukan kunci untuk dienkripsi terdiri dari 1 huruf : ")
key = input("-> : ")
print(Style.RESET_ALL)
gabungan_saya = {}
lis_n_saya = []
for k in kalimat:
    gabungan_saya[k] = gabungan[k]
    lis_n_saya.append(gabungan[k])
#membuat kunci
gabungan_saya_key = []
for lis in range(len(kalimat)) :
    gabungan_saya_key.append(gabungan[key[0]])
#aturan enkripsi
#(p+k)mod26
mod = []
hasil_mod_enkripsi = []
for n_kalimat in range(len(lis_n_saya)) :
    hasil = (lis_n_saya[n_kalimat] + gabungan_saya_key[n_kalimat]) % 26
    mod.append(hasil)
for exs in mod:
    hasil_mod_enkripsi.append(abjat[exs])
print("===========================")
print(Fore.YELLOW)
print('Hasil enkripsi melalui proses')
print(mod)
print(hasil_mod_enkripsi)
print("-> hasilnya : ")
print(''.join(hasil_mod_enkripsi))