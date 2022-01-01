import matplotlib.pyplot as plt
from random import uniform,randint
import pandas as pd
import numpy as np
from scipy.stats import norm
domain = np.arange(1,1001)
reang = 5*np.random.randn(1000)+10
fig,pt = plt.subplots(1,3)
pt[0].scatter(domain,reang)
pt[1].hist(reang)
plt.show()
