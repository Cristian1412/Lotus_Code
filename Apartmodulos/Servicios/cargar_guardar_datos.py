import json

def cargar_datos_servicios(archivo):
    datos_servicios = {}
    with open(archivo,"r") as file:
        datos_servicios=json.load(file)
    return datos_servicios
        
        

def guardar_datos_servicios(datos_servicios, archivo):
    datos_servicios = dict(datos_servicios)
    diccionario=json.dumps(datos_servicios, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()