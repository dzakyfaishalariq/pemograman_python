import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd
import os
import seaborn as sns
from scipy.stats import norm
sns.set()
os.system('cls')
data = 5*np.random.randn(1000) + 10
data2 = np.arange(-3, 3, 0.001)
y = norm.pdf(data2, 0, 1)
print(data.var())
print(data.mean())
fig, pt = plt.subplots(1, 2)
pt[0].hist(data)
pt[1].plot(data2, y, 'g--')
plt.show()
