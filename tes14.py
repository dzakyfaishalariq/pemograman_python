import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
os.system('cls')
habis_dibagi20 = 0
habis_dibagi4 = 0
habis_dibagi5 = 0
h20 = []
h4 = []
h5 = []
for i in range(0, 50):
    if i % 20 == 0:
        print("nilai ini habis dibagi 20 aja : {}".format(i))
        print('-+-+-')
        habis_dibagi20 += 1
        h20.append(i)
    if i % 4 == 0:
        print("nilai ini habis di bagi 4 aja: {}".format(i))
        print('-+-+-')
        habis_dibagi4 += 1
        h4.append(i)
    if i % 5 == 0:
        print("nilai ini habis di bagi 5 aja: {}".format(i))
        print('-+-+-')
        habis_dibagi5 += 1
        h5.append(i)
print('himpunan 20 : {}'.format(h20))
print('himpunan 4  : {}'.format(h4))
print('himpunan 5  : {}'.format(h5))
print('jumlah H20 : {}, jumlah H4 : {}, jumlah H5: {}'.format(
    habis_dibagi20, habis_dibagi4, habis_dibagi5))
fig, pt = plt.subplots()
pt.bar(['H20', 'H4', 'H5'], [habis_dibagi20, habis_dibagi4, habis_dibagi5])
plt.show()
