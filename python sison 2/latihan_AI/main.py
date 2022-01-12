"""
Sebuah Perusahaan dperakit CPU mempunyai data-data sebagai berikut:
a. permintaan terbesar mencapai 1000 unit dan terkecil 200 unit perhari
b. Persediaan digudang terbanyak 120 unit dan terkecil 20 unit perhari
c. Produksi maksimum 1400 unit dan minimum 400 unit perhari
Berapa CPU harus di rakit bila jumlah permintaan 800 unit dan
persediaan gudang ada 60 unit, bila proses tersebut
di tentukan dengan aturan fuzziy
-> if permintaan (Turun) and persediaan(banyak):
    then produksi (berkurang)
-> if permintaan (naik) and persediaan(sedikit):
    then produksi (bertambah)
-> if permintaan (naik) and persediaan(banyak):
    then produksi (bertambah)
-> if permintaan (Turun) and persediaan(sedikit):
    then produksi (berkurang)
"""
import numpy as np
from fuzzy.fuzzyPermintaan import fungsiPermintaan, keanggotaan_permintaan
from fuzzy.persediaan import fungsipersediaan, keanggotaan_persediaan
from fuzzy.fuzzyProduksi import fungsiperoduksi
import os
os.system('cls')


def range_x(a, b, c):
    lintasan = np.arange(a, b, c)
    return lintasan


rang_permintaan = range_x(0, 1501, 1)
rang_rule_permintaan = np.array([
    [0, 1, 200, 1000],
    [200, 1000, 1401, 1501]
])
turun, naik = fungsiPermintaan(
    rang_permintaan,
    rang_rule_permintaan,
    "Fungsi Permintaan",
    "Turun",
    "Naik"
)
v_turun, v_naik = keanggotaan_permintaan(
    rang_permintaan,
    turun,
    naik,
    800
)
rang_persediaan = range_x(0, 125, 1)
rang_rule_persediaan = np.array(
    [
        [0, 1, 20, 100],
        [20, 100, 120, 124]
    ]
)
kecil, banyak = fungsipersediaan(
    rang_persediaan,
    rang_rule_persediaan,
    'Tabel Persediaan',
    'kecil',
    'banyak'
)
v_kecil, v_banyak = keanggotaan_persediaan(
    rang_persediaan,
    kecil,
    banyak,
    60
)
rang_produksi = range_x(0, 1700, 1)
rang_rule_produksi = np.array([
    [0, 1, 200, 1200],
    [400, 1400, 1600, 1669]
])
berkurang, bertambah = fungsiperoduksi(
    rang_produksi,
    rang_rule_produksi,
    'fungsi produksi',
    'berkurang',
    'bertambah'
)
# pengoprasian fungsi
# rumus yang digunakan
"""
(berkurang) => (1200-x)/(1000)
v_turun     => (1200-z)/(1000)
(v_turun * 1000) => 1200 - z
(v_turun * 1000) - 1200 => -z
z => 1200 - (v_turun * 1000)
******
(bertambah) => (z - 400)/(1400-400)
v_turun*1000 => z-400
z => (v_turun * 1000) + 400
"""
nilai1 = min(v_turun, v_banyak)
z1 = 1200-(nilai1*1000)  # berkurang
nilai2 = min(v_naik, v_kecil)  # if v_naik and v_kecil:
z2 = (nilai2*1000)+400  # bertambah
nilai3 = min(v_naik, v_banyak)  # if v_naik and v_banyak:
z3 = (nilai3*1000)+400  # bertambah
nilai4 = min(v_turun, v_kecil)  # if v_turun and v_kecil:
z4 = 1200-(nilai4*1000)  # berkurang
hasil_akhir = ((nilai1*z1)+(nilai2*z2)+(nilai3*z3) +
               (nilai4*z4))/(nilai1+nilai2+nilai3+nilai4)
print(v_turun)
print(v_naik)
print('===========')
print(v_kecil)
print(v_banyak)
print("===========")
print('{},{},{},{}'.format(z1, z2, z3, z4))
print("Maka CPU yang harus di rakit iyalah \n: {}".format(
    int(hasil_akhir)))
