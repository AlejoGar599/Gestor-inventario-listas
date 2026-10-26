import sys

productos = []
cantidades = []


def Registrar_Producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    for i in range(len(productos)):
        
        if productos[i].lower() == nombre.lower():
            print("El producto ya se encuentra registrado.")
            return
        
    cantidad = int(input("Cantidad disponible: "))
    
    if cantidad < 0:
        print("La cantidad no puede ser menor que 0")
        return
    
    productos.append(nombre)
    cantidades.append(cantidad)
    
    print("El producto ", nombre, "se ha registrado correctamente.")
    return


def Mostrar_Inventario():
    
    print("====INVENTARIO====")
    
    for i in range(len(productos)):
        print(i + 1, productos[i], "-", cantidades[i])
    return


def Buscar_Producto():
    nombre = input("Nombre del producto a buscar: ").strip()
    
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            print("Producto:", productos[i])
            print("Cantidad disponible:", cantidades[i])
            return
        
    print("El producto no se encuentra en el inventario.")
    return


def Modificar_Cantidad():
    nombre = input("Nombre del producto a modificar: ").strip()
    
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            print("Cantidad actual:", cantidades[i])
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return
            
            cantidades[i] = nueva_cantidad
            
            print("Cantidad modificada correctamente.")
            return
        
    print("El producto no se encuentra en el inventario.")
    return


def Eliminar_Producto():
    nombre = input("Nombre del producto a eliminar: ").strip()
    
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            productos.pop(i)
            cantidades.pop(i)
            
            print("Producto eliminado correctamente.")
            return
        
        
    print("El producto no se encuentra en el inventario.")
    return


def Contar_Productos():
    print("Lista de productos distintos registrados:", len(productos))
    return


def Producto_Mayor_Cantidad():
    if len(productos) == 0:
        print("El inventario esta vacio.")
        return
    
    mayor = cantidades[0]
    posicion = 0
    
    for i in range(1, len(cantidades)):
        if cantidades[i] > mayor:
            mayor = cantidades[i]
            posicion = i
            
    print("Producto con mayor cantidad:", productos[posicion])
    print("Cantidad disponible:", cantidades[posicion])
    return


def menu():
    while True:
        print("=======GESTOR DE INVENTARIO=======")
        print("1.Registrar un producto")
        print("2.Mostrar inventario")
        print("3.Buscar un producto")
        print("4.Modificar cantidad")
        print("5.Eliminar un producto")
        print("6.Contar productos distintos")
        print("7.Mostrar producto con mayor cantidad")
        print("8.Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            Registrar_Producto()

        elif opcion == "2":
            Mostrar_Inventario()

        elif opcion == "3":
            Buscar_Producto()

        elif opcion == "4":
            Modificar_Cantidad()

        elif opcion == "5":
            Eliminar_Producto()

        elif opcion == "6":
            Contar_Productos()

        elif opcion == "7":
            Producto_Mayor_Cantidad()

        elif opcion == "8":
            print("Saliendo del programa")
            sys.exit()

        else:
            print("Opcion no valida, intente nuevamente")
menu()
