indo = ["satu","dua","tiga","empat"]
ingr = ["one","two","tree","four"]
print("Isikan teks indonesianya")
x = int(input("teks indonesia : "))
i = 0
while i < len(indo):
    if i == x:
        print("Bahasa indonesianya : " , indo[i])
        print("bahasa ingrisnya    : " , ingr[i])
    i = i + 1