from colorama import Fore,Style
import colorama
nilai = (int(input('nilai : ')))
print(Fore.BLUE)
print("Hallo apa kabar {}".format(nilai))
if nilai >= 80:
    print("Kamu lulus")
else:
    print('maaf salah input')    
print(Style.RESET_ALL)
