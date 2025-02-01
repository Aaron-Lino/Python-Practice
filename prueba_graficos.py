import matplotlib.pyplot as plt
import numpy as np
#los datos o las graficas mostradas no son reales debido a que este es un documento de prueba
x = np.arange(-12,13,1)
y = x * np.sin(x)

plt.plot(x,y)
plt.ylabel('porcentaje anual')
plt.xlabel('Año fiscal')
plt.title('Crecimiento del PIB ecuatoriano (2015-2023)')
plt.show()