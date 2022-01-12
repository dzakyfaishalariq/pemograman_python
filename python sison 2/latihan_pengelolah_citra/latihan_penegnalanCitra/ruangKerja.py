from Library_saya import atribut as atr
from colorama import Fore, Back, Style
import os
os.system('cls')
os.chdir('C:/Users/Dzaky Faihalariq Pir/Downloads/pythonseson2/latihan_pengelolah_citra/img')
data = os.listdir()

citra = atr.pengolahanCitra(data[0])
citra.negatif()

print(Fore.RED + 'Sudah selesai')
print(Fore.GREEN + 'Selamat')
print(Style.RESET_ALL)
print('='*25)
