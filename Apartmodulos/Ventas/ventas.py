from Apartmodulos.Ventas.datos import *
from Apartmodulos.Servicios.servicios import *
from Apartmodulos.Servicios.cargar_guardar_datos import *

RUTA_CENTRAL = "Apartmodulos/Administrativo/usurandnameCRUD.json"
RUTA_DE_VENTAS = "Apartmodulos/Ventas/lovendido.json"
RUTA_SERVICIOS = "Apartmodulos/Servicios/SERVICIYPRODUCT.json"

datos = cargar_datos_ventas(RUTA_CENTRAL)
datos_ventas = cargar_datos_ventas(RUTA_DE_VENTAS)


def ventas_totales(datos:dict):
    for i in datos["usuarios"]:
        if "servicios" in i:
            print(i["servicios"])
    
    

def interacciones_servicios(datos_ventas:dict):
    
    try:
        opc = int(input("Ingrese 1 para comprar un servicio: "))
    except Exception:
        opc = 0
    finally:
        if opc == 1:
            for i in range(len(datos_ventas["ventas"])):
                servicio={}
                servicio["servicio adquirido"]=input("Ingrese el servicio: ")
                        
    datos_ventas["ventas"].append(servicio)
    return datos_ventas

def interacciones_productos(datos_ventas:dict):
    
    try:
        opc = int(input("Ingrese 1 para comprar un servicio: "))
    except Exception:
        opc = 0
    finally:
        if opc == 1:
            for i in range(len(datos_ventas["ventas"])):
                producto={}
                producto["producto adquirido"]=input("Ingrese el producto: ")
                        
    datos_ventas["ventas"].append(producto)
    return datos_ventas
            

datos = guardar_datos_servicios(datos, RUTA_DE_VENTAS)
guardar_datos_ventas(datos_ventas, RUTA_DE_VENTAS)

