import json

def cargar_datos_ventas(archivo):
    datos_ventas = {}
    with open(archivo,"r") as file:
        datos_ventas=json.load(file)
    return datos_ventas
        
        

def guardar_datos_ventas(datos_ventas, archivo):
    datos_ventas = dict(datos_ventas)
    diccionario=json.dumps(datos_ventas, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()