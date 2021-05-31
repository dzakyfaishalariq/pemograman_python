a = [[1,2,3],
     [2,3,4],
     [3,4,5]]
b = [[3,4,5],
     [4,5,6],
     [5,6,7]]
hasil = [[],
         [],
         []]
for i in range(0, 3):
    for j in range(0,3):
        print(a[i][j], end=" ")
    print(" ")
print()
print()
for i in range(0, 3):
    for j in range(0,3):
        print(b[i][j], end=" ")
    print(" ")
print()
print("======================(+)")
for i in range(0, 3):
    for j in range(0,3):
        hasil = a[i][j] + b[i][j]
        print(hasil , end="\t")
    print(" ")
    print(" ")