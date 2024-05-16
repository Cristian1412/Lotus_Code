def creacion_de_usuario(datos:dict):
    usuario={}
    usuario["nombre"]=input("Ingrese tu nombre: ")
    usuario["documento"]=input("Ingrese su documento: ")
    usuario["activo o inactivo"]= ("activo")
    usuario["activo o inactivo"]= input("Por favor ingrese el servicio que quiere adquirir:  ")
    try:
        usuario["rango de edad"] = int(input("Ingresa tu edad: "))
    except Exception:
        usuario["rango de edad"] = 0
    try:
        usuario["codigo"] = int(input("Ingrese el codigo: "))
    except Exception:
        usuario["codigo"] = 0
    try:
        usuario["numero telefonico"] = int(input("Ingresa tu número de telefono: "))
    except Exception:
        usuario["numero telefonico"] = ""
    datos["usuarios"].append(usuario)
    print("usuario registrado")
    print(datos)
    return datos

def leer_datos_usuario(datos):
    documento = input("Ingrese el número de documento del usuario: ")
    for i in datos["usuarios"]:
        if i["documento"] == documento:
            for llave,valor in i.items():
                print(llave,"=", valor)
    

        

def actualizar_datos_usuario(datos:dict):
    
    documento = input("ingrese el documento del usuario para actualizarlo: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            usuario={}
            usuario["nombre"]=input("Ingrese el nombre: ")
            usuario["documento"]=input("Ingrese el documento: ")
            usuario["estado"]= input("Ingrese estado del usuario: ")
            usuario["servicios"]= input("Ingrese el servicio que desee adquirir:  ")
            try:
                usuario["edad"] = int(input("Ingrese la edad: "))
            except Exception:
                usuario["edad"] = 0
            try:
                usuario["codigo"] = int(input("Ingrese el codigo: "))
            except Exception:
                usuario["codigo"] = 0
            try:
                usuario["numero telefonico"] = int(input("Ingrese su numero telefonico: "))
            except Exception:
                usuario["numero telefonico"] = ""
            datos["usuarios"][i].update(usuario)
        return datos



def eliminar_datos_usuario(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
                datos["usuarios"].pop(i)
                print("Eliminado")
    return datos
        
def categoria_usuario(datos):
    
    codigo =input("Ingrese el codigo: ")
    
    
    if codigo == "1" or "2" or "3" or "4" or "5":
                print("Usuario leal")
    elif codigo == "6" or "7" or "8" or "9" or "10":
                print("Usuario nuevo")
    





