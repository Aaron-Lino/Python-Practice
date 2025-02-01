import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10,1)
y = x * np.sin(x)

plt.plot(x,y)
plt.show()