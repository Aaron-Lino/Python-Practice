text = input("Introduce el texto a analizar: ").lower()
Letter = list(input("Porfavor intucuce 3 letras: ").lower())

cantidad_Letras1 = text.count(Letter[0])
cantidad_Letras2 = text.count(Letter[1])
cantidad_Letras3 = text.count(Letter[2])

print(f"la cantida total de la letra {Letter[0]} es {cantidad_Letras1}")
print(f"la cantida total de la letra {Letter[1]} es {cantidad_Letras2}")
print(f"la cantida total de la letra {Letter[2]} es {cantidad_Letras3}")

total = text.split()

print(f"La cantidad total de palabras es {len(total)}")

print(f"La primera letra fue {text[0]} y la ultima fue {text[-1]}")
total.reverse()
text_alrevez = ' '.join(total)

print(f"El texto alrevez diria {text_alrevez}")

buscar = input("Digita la palabra a buscar: ")

misssing_word = buscar in text
verifier = {True:"Si", False:"No"}
print(f"La palabra a buscar '{buscar}' {verifier[misssing_word]} se encuentra en el texto")