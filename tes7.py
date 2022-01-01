# regresion
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
sns.set()
os.system('cls')
data = pd.read_csv('Iris.csv')
data_id = np.array(data['Id'])
data_y = np.array(data['SepalWidthCm'])
a = 0
b = 0
c = 0
d = 0
e = 0
for i in data_id:
    a += i*data_y[i-1]
    b += i
    c += data_y[i-1]
    d += i**2
    e += i
nilai_b = ((150*a) - (b*c))/((150*d)-(e**2))
nilai_a = ((c/150)-nilai_b*(b/150))
y = nilai_b*data_id + nilai_a

fig, pt = plt.subplots()
pt.scatter(data['Id'], data['SepalWidthCm'])
pt.plot(data_id, y)
plt.grid()
plt.show()
