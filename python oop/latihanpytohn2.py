from typing import ForwardRef


print("Membuat aturan segitiga")
print("=======================")
b = 10
for x in range(0,b):
    for y in range(0,x+1):
        print("* ",end=" ")# ini adalah membuat perulangan secara horizontal
    print("")
print("======================")
print("======================")
a = 10
c = 2*a-2
for i in range(0,a):
    for j in range(0,c):
        print("",end=" ")
    c -=2
    for j in range(0,i+1):
        print("*", end=" ")
    print("")

