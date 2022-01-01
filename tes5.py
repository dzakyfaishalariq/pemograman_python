from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = np.array([67,67,64,64,74,61,68,71,69,61,65,64, 
62,63,59,70,66,66,63,59,64,67,70,65, 
66,66,56,65,67,69,64,67,68,67,67,65,74,64,62,68,65,65,65,66,67])
print(max(data))
print(min(data))
fig,pt = plt.subplots()
pt.hist(data,6)
plt.show()