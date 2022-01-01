import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

x = np.arange(-3,3,0.01)
y = norm.pdf(x,0,1)
plt.scatter(x,y)
plt.plot(x,y)
plt.show()