import pandas as pd
import matplotlib.pyplot as plt

width = 0.25

workbook = "puntajes.xlsx" #here put the file you want
df = pd.read_excel(workbook)
print(df.head())

datos = df[["name","Algebra","Quimica"]]

#datos.plot.bar(x = "name", y = "Algebra", color = "green", width = width, rot=0)
datos.plot(x = "name", kind = "bar", rot = 0)
plt.title("Grafico Excel")
plt.xlabel("Nombres")
plt.ylabel("Puntajes")
plt.grid()
plt.show()