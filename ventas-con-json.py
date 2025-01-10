import json


def cargar_inventario(archivo='inventario.json'):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar_inventario(inventario, archivo='inventario.json'):
    with open(archivo, 'w') as f:
        json.dump(inventario, f, indent=4)


def agregar_producto(inventario):
    try:
        id = int(input("Ingrese el ID del producto: "))
        if any(prod['ID'] == id for prod in inventario):
            print("Error: El ID ya existe.")
            return
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        inventario.append({"ID": id, "Nombre": nombre, "Cantidad": cantidad, "Precio": precio})
        print("Producto agregado exitosamente.")
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar números donde corresponda.")


def eliminar_producto(inventario):
    try:
        id = int(input("Ingrese el ID del producto a eliminar: "))
        for prod in inventario:
            if prod['ID'] == id:
                inventario.remove(prod)
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")
    except ValueError:
        print("Error: ID inválido.")


def actualizar_producto(inventario):
    try:
        id = int(input("Ingrese el ID del producto a actualizar: "))
        for prod in inventario:
            if prod['ID'] == id:
                print(f"Producto encontrado: {prod['Nombre']}")
                cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
                if cantidad:
                    prod['Cantidad'] = int(cantidad)
                if precio:
                    prod['Precio'] = float(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")
    except ValueError:
        print("Error: Entrada inválida.")


def ver_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("\n--- Inventario ---")
    for prod in inventario:
        print(
            f"ID: {prod['ID']}, Nombre: {prod['Nombre']}, Cantidad: {prod['Cantidad']}, Precio: ${prod['Precio']:.2f}")


def buscar_producto(inventario):
    termino = input("Ingrese el nombre o ID del producto a buscar: ")
    encontrado = False
    for prod in inventario:
        if str(prod['ID']) == termino or prod['Nombre'].lower() == termino.lower():
            print(
                f"ID: {prod['ID']}, Nombre: {prod['Nombre']}, Cantidad: {prod['Cantidad']}, Precio: ${prod['Precio']:.2f}")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.")


def calcular_valor_total(inventario):
    total = sum(prod['Cantidad'] * prod['Precio'] for prod in inventario)
    print(f"Valor Total del Inventario: ${total:.2f}")


def main():
    inventario = cargar_inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Ver Inventario")
        print("5. Buscar Producto")
        print("6. Calcular Valor Total")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            eliminar_producto(inventario)
        elif opcion == '3':
            actualizar_producto(inventario)
        elif opcion == '4':
            ver_inventario(inventario)
        elif opcion == '5':
            buscar_producto(inventario)
        elif opcion == '6':
            calcular_valor_total(inventario)
        elif opcion == '7':
            guardar_inventario(inventario)
            print("Inventario guardado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
