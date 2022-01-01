import matplotlib.pyplot as plt
import numpy as np
import os
print("hallo word")
x = np.linspace(-5,5,100)
y = x ** 2 + x + 6
fig,pt = plt.subplots()
pt.plot(x,y)
plt.axis([-6,6,-25,25])
plt.show()