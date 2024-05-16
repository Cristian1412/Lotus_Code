from Apartado_de_registro.registros import registrar_excepcion
from Apartmenu.principal_menu import menu_principal, menu_reportes, menu_servicios, menu_usuarios, menu_ventas, pedir_opcion
from Apartmodulos.Administrativo.usuarios import actualizar_datos_usuario, categoria_usuario, creacion_de_usuario, eliminar_datos_usuario, leer_datos_usuario
from Apartmodulos.Servicios.cargar_guardar_datos import guardar_datos_servicios
from Apartmodulos.Servicios.servicios import actualizar_producto, actualizar_servicio, cant_product, cant_servic, eliminar_producto, eliminar_servicio, generar_producto, generar_servicio, listar_servicios
from Apartmodulos.Ventas.datos import cargar_datos_ventas, guardar_datos_ventas
from Apartmodulos.Ventas.ventas import interacciones_productos, interacciones_servicios, ventas_totales


RUTA = "Apartmodulos/Administrativo/usurandnameCRUD.json"
RUTA_SERVICIOS = "Apartmodulos/Servicios/SERVICIYPRODUCT.json"
RUTA_REGISTROS = "registro.txt"
RUTA_VENTAS = "Apartmodulos/Ventas/lovendido.json"

def cargar_datos (ruta):
    return[]
datos_servicios = cargar_datos(RUTA_SERVICIOS)
datos_servicios = cargar_datos(RUTA_SERVICIOS)
datos = cargar_datos(RUTA)
datos_ventas = cargar_datos_ventas(RUTA_VENTAS)


while True:
    menu_principal()
    opc = pedir_opcion()
    
    if opc == 1:
        print(menu_usuarios())
        opc = pedir_opcion()
        if opc == 1:
            datos = creacion_de_usuario(datos)
        elif opc == 2:
            datos = leer_datos_usuario(datos)
        elif opc == 3:
            datos = actualizar_datos_usuario(datos)
        elif opc == 4:
            datos = eliminar_datos_usuario(datos)
        elif opc == 5:
            datos= categoria_usuario(datos)
        
        

    elif opc == 2:
        
        print(menu_servicios())
        opc = pedir_opcion()
        if opc == 1:
            datos_servicios = generar_servicio(datos_servicios)
            datos_servicios = generar_producto(datos_servicios)
        elif opc == 2:
            listar_servicios(datos_servicios)
        elif opc == 3:
            datos_servicios = actualizar_servicio(datos_servicios)
            datos_servicios = actualizar_producto(datos_servicios)
        elif opc == 4:
            datos_servicios = eliminar_servicio(datos_servicios)
            datos_servicios = eliminar_producto(datos_servicios)
            
    elif opc == 3:
        print(menu_reportes())
        opc = pedir_opcion()
        if opc == 1: 
            cant_servic(datos_servicios)
        cant_product(datos_servicios)

    elif opc == 4:
        print(menu_ventas())
        opc = pedir_opcion()
        if opc == 1:
            ventas_totales(datos)
        elif opc == 2:
            datos_ventas = interacciones_productos(datos_ventas)
        elif opc == 3:
            datos_ventas = interacciones_servicios(datos_ventas)

    elif opc == 5:
        print("Acabas de salir!!")
        break

    registrar_excepcion(Exception)
    
    (cargar_datos, RUTA)
    guardar_datos_servicios(datos_servicios, RUTA_SERVICIOS)
    guardar_datos_ventas(datos_ventas, RUTA_VENTAS)