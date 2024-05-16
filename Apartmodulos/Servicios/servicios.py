def generar_servicio(datos_servicios):
    servicio={}
    servicio["id"]=input("Ingrese el ID del servicio: ")
    servicio["nombre"]=input("Ingrese el nombre: ")
    servicio["caracteristicas"]=input("Ingrese las características: ")
    try:
        servicio["precio"] = int(input("Ingrese el precio: "))
    except Exception:
        servicio["precio"] = 0
    
    datos_servicios["servicios"].append(servicio)
    print("servicio registrado")
    print(datos_servicios)
    return datos_servicios

def generar_producto(datos_servicios):
    producto={}
    producto["id"]=input("Ingrese id del producto: ")
    producto["nombre"]=input("Ingrese el nombre: ")
    producto["caracteristicas"]=input("Ingrese las características: ")
    try:
        producto["precio"] = int(input("Ingrese el precio: "))
    except Exception:
        producto["precio"] = 0
    
    datos_servicios["productos"].append(producto)
    print("producto registrado")
    print(datos_servicios)
    return datos_servicios
    
def listar_servicios(datos_servicios):
    for i in datos_servicios["servicios"]:
        for llave,valor in i.items():
            print(llave,"=", valor)

def actualizar_servicio(datos_servicios):
    datos_servicios = dict(datos_servicios)
    nombre =input("Ingrese el nombre: ")
    for i in range(len(datos_servicios["servicios"])):
        if datos_servicios["servicios"][i]["nombre"] == nombre:
            servicio={}
            servicio["id"]=input("Ingrese id del servicio: ")
            servicio["nombre"]=input("Ingrese el nombre: ")
            servicio["caracteristicas"]=input("Ingrese las características: ")
            try:
                servicio["precio"] = int(input("Ingrese el precio: "))
            except Exception:
                servicio["precio"] = 0
            datos_servicios["servicios"][i].update(servicio)
        return datos_servicios
    
def actualizar_producto(datos_servicios):
    datos_servicios = dict(datos_servicios)
    nombre =input("Ingrese el nombre: ")
    for i in range(len(datos_servicios["productos"])): 
      if datos_servicios["productos"][i]["nombre"] == nombre:
        producto={}
        producto["id"]=input("Ingrese id del producto: ")
        producto["nombre"]=input("Ingrese el nombre: ")
        producto["caracteristicas"]=input("Ingrese las características: ")
        try:
            producto["precio"] = int(input("Ingrese el precio: "))
        except Exception:
            producto["precio"] = 0
        datos_servicios["productos"][i].update(producto)
    return datos_servicios

def eliminar_servicio(datos_servicios):
    datos_servicios = dict(datos_servicios)
    nombre =input("Ingrese el nombre: ")
    for i in range(len(datos_servicios["servicios"])):
        if datos_servicios["servicios"][i]["nombre"] == nombre:
                datos_servicios["servicios"].pop(i)
                print("Eliminado")
    return datos_servicios

def eliminar_producto(datos_servicios):
    datos_servicios = dict(datos_servicios)
    nombre =input("Ingrese el nombre: ")
    for i in range(len(datos_servicios["productos"])):
        if datos_servicios["productos"][i]["nombre"] == nombre:
                datos_servicios["productos"].pop(i)
                print("Eliminado")
    return datos_servicios

def cant_servic(datos_servicios:dict):
    
    for i in range(len(datos_servicios["servicios"])):
        result = i+1
        print(result,"servicios")

def cant_product(datos_servicios:dict):
    
    for i in range(len(datos_servicios["productos"])):
        result = i+1
        print(result,"productos")

