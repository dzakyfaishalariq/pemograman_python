import os
from colorama import Fore,Style
nilai = 10
os.system('cls')
for i in range(nilai):
    if i % 2 == 0:
        print(Fore.GREEN)
        for j in range(i):
            print("*",end='  ')
        print(Style.RESET_ALL)
    else:
        print(Fore.YELLOW)
        for j in range(i):
            print("*",end='  ')
        print(Style.RESET_ALL)
    print()
