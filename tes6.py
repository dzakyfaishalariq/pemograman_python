from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = np.array(
[68, 84, 75, 82, 68, 90, 62, 88, 76, 93,
73, 79, 88, 73, 60, 93, 71, 59, 85, 75,
61,65, 75, 87, 74, 62, 95, 78, 63, 72,
66, 78, 82, 75, 94, 77, 69, 74, 68 ,60,
96, 78, 89, 61, 75, 95, 60, 79, 83, 71,
79, 62, 67, 97, 78, 85, 76, 65, 71, 75,
65, 80, 73, 57, 88, 78, 62, 76, 53, 74,
86, 67, 73, 81, 72, 63, 76, 75, 85, 77])
print(max(data))
print(min(data))
fig,pt = plt.subplots()
pt.hist(data,10)
plt.show()