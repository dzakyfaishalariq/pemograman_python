import os
os.system('cls')
try:
    tinggi = int(input('masukan tinggi : '))
    for t in range(tinggi):
        for k in range(t):
            print('', end=' ')
        for i in range(tinggi):
            print('*', end=' ')
        tinggi -= 1
        print()
except:
    print('maaf ada kessalah error di input pemasukan')

print('a', end='')
print('b')
