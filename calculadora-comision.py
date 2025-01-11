nombre = input("Ingrese su nombre: ")
Ventas = float(input("Ingrese el valor total de sus ventas: $"))
comision = round(Ventas * 13/100,2)
print(f"Estimado {nombre}, gracias a las ventas totales del año pur un valor de {Ventas} su comision (calculada al 13%) es de: {comision}")