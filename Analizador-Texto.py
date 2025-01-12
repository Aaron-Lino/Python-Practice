texto = input("ingrese un texto: ")
letras = []
texto = texto.lower()

letras.append(input("introduce la primera letra: ").lower())
letras.append(input("introduce la segunda letra: ").lower())
letras.append(input("introduce la tercera letra: ").lower())

print("\nCONTADOR")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"La letra {letras[0]} se repite un total de {cantidad_letras1} veces")
print(f"La letra {letras[1]} se repite un total de {cantidad_letras2} veces")
print(f"La letra {letras[2]} se repite un total de {cantidad_letras3} veces")

print("\nNUMERO TOTAL DE PALABRAS")
total = texto.split()
print(f"En el texto se encuentra un numero total de {len(total)} palabras")

print("\n primera y ultima palabra")
primera_pal = texto[0]
ultima_pal = texto[-1]
print(f"La primera letra fue la {primera_pal} y la ultima fue {ultima_pal}")

print("\n por si te interesa tu texto a la inversa: ")
total.reverse()
texto_invertido = ' '.join(total)
print(f"Tu texto a la inversa es: {texto_invertido}")

print("Verificador de palabra")
palabra = "python" in texto
dic_texto = {True:"Si", False:"No"}
print(f"La palabra 'python {dic_texto[palabra]} se encuentra en el texto")