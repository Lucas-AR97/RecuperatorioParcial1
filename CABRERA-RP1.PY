def agregar_producto(nombres, cantidades):
    """Agrega un nuevo producto al stock."""
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))
    nombres.append(nombre)
    cantidades.append(cantidad)
    print("Producto agregado con éxito.")

def ver_productos_agotados(nombres, cantidades):
    """Muestra los productos con stock agotado (cantidad = 0)."""
    print("Productos agotados:")
    agotados = False
    for i in range(len(nombres)):
        if cantidades[i] == 0:
            print(nombres[i])
            agotados = True
    if not agotados:
        print("No hay productos agotados.")

def actualizar_stock(nombres, cantidades):
    """Actualiza la cantidad en stock de un producto existente."""
    producto = input("Ingrese el nombre del producto a actualizar: ")
    if producto in nombres:
        index = nombres.index(producto)
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        cantidades[index] = nueva_cantidad
        print("Stock actualizado.")
    else:
        print("Producto no encontrado.")

def ver_todos_los_productos(nombres, cantidades):
    """Muestra el listado completo de productos con su stock."""
    print("Listado de productos:")
    for i in range(len(nombres)):
        print(f"{nombres[i]}: {cantidades[i]}")

def menu():
    """Muestra el menú de opciones y gestiona la interacción con el usuario."""
    nombres = []
    cantidades = []
    salir = False

    while not salir:
        print("\nMenú de opciones:")
        print("1. Agregar producto")
        print("2. Ver productos agotados")
        print("3. Actualizar stock")
        print("4. Ver todos los productos")
        print("5. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            agregar_producto(nombres, cantidades)
        elif opcion == "2":
            ver_productos_agotados(nombres, cantidades)
        elif opcion == "3":
            actualizar_stock(nombres, cantidades)
        elif opcion == "4":
            ver_todos_los_productos(nombres, cantidades)
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            salir = True
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()