import os
os.system('cls')
def jumlah(a):
    if a <= 10:
        print(a,end="")
        n = a+1
        jumlah(n)
def pangkat(b):
    if b <= 5:
        m = 2**b
        print(m, end= " ")
        pangkat(b+1)
pangkat(1)

pi = 3.14
r = 10
d = 20
luas = pi*d/2*d/2
print('\n')
print(luas)