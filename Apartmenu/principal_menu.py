def menu_principal():
    print("**************************************************")
    print("Bienvenido a nuestro menú de Claro\n te presentamos las siguientes opciones")
    print("**************************************************")
    print("Ingrese la opción que requiera")
    print("1. para ir al apartado administrativo de los usuarios")
    print("2. para ir al apartado administrativo de  los servicios")
    print("3. para ir al apartado de reportes")
    print("4. para ir al apartado de ventas")
    print("5. salir")
    print("**************************************************")

def menu_usuarios():
    print("**************************************************")
    print("Ingrese la opción que necesite")
    print("1. crear un usuario")
    print("2. ver informacion de un usuario")
    print("3. actualizar a un usuario")
    print("4. eliminar un usuario")
    print("5. ver la categoria del usuario")
    print("**************************************************")

def menu_servicios():
    print("Ingrese la opción que requiera")
    print("1. crear un servicio")
    print("2. ver el catalogo de servicios")
    print("3. actualizar un servicio")
    print("4. eliminar un servicio")
    print("**************************************")

def menu_ventas():
    print("***********************************************")
    print("Ingrese la opción que requiera")
    print("1. ver el registro de ventas totales")
    print("2. comprar un producto")
    print("3. comprar un servicio")
    print("***********************************************")
    
def menu_reportes():
    print("**********************************************")
    print("Ingrese la opción que requiera")
    print("1. ver la cantidad de productos y servicios que hay en la empresa")
    print("***********************************************")


def pedir_opcion():
    resultado_opc = 0
    try:
        resultado_op = int(input("Ingrese una opción: "))
        print("******************")
        return resultado_opc
    except Exception:
        print("El valor inválido")
        print("******************")
        return -1