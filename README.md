# Sistema de Gestión de Usuarios, Servicios y Ventas

## Descripción

Este proyecto es una aplicación de línea de comandos que permite la gestión de usuarios, servicios y ventas. Está diseñado para ser utilizado en una empresa que necesita llevar un registro detallado de sus usuarios, los servicios y productos que ofrece, y las ventas realizadas. La aplicación proporciona menús interactivos para administrar estas entidades y sus respectivas operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## Características

- *Gestión de Usuarios*:
  - Crear usuario
  - Ver información de usuario
  - Actualizar usuario
  - Eliminar usuario
  - Ver categoría del usuario según su código

- *Gestión de Servicios y Productos*:
  - Crear servicio
  - Listar servicios
  - Actualizar servicio
  - Eliminar servicio
  - Crear producto
  - Listar productos
  - Actualizar producto
  - Eliminar producto
  - Contar cantidad de servicios y productos

- *Gestión de Ventas*:
  - Ver registro de ventas totales
  - Registrar la compra de un producto
  - Registrar la compra de un servicio

## Estructura del Proyecto


Apartmodulos/
├── Administrativo/
│   └── usurandnameCRUD.json
├── Ventas/
│   ├── datos.py
│   ├── lovendido.json
│   └── ventas.py
├── Servicios/
│   ├── cargar_guardar_datos.py
│   ├── servicios.py
│   └── SERVICIYPRODUCT.json
├── main.py
└── README.md


## Instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. Instala las dependencias necesarias (si aplica).

sh
git clone <repositorio_url>
cd <directorio_del_proyecto>
pip install -r requirements.txt  # Si hay un archivo requirements.txt


## Uso

1. *Cargar y Guardar Datos*:
   python
   from Apartmodulos.Servicios.cargar_guardar_datos import cargar_datos_servicios, guardar_datos_servicios
   from Apartmodulos.Ventas.datos import cargar_datos_ventas, guardar_datos_ventas

   RUTA_CENTRAL = "Apartmodulos/Administrativo/usurandnameCRUD.json"
   RUTA_DE_VENTAS = "Apartmodulos/Ventas/lovendido.json"
   RUTA_SERVICIOS = "Apartmodulos/Servicios/SERVICIYPRODUCT.json"

   datos = cargar_datos_servicios(RUTA_CENTRAL)
   datos_ventas = cargar_datos_ventas(RUTA_DE_VENTAS)
   

2. *Operaciones CRUD para Usuarios*:
   python
   from Apartmodulos.Servicios.servicios import *

   # Crear usuario
   datos = creacion_de_usuario(datos)

   # Leer datos de usuario
   leer_datos_usuario(datos)

   # Actualizar usuario
   datos = actualizar_datos_usuario(datos)

   # Eliminar usuario
   datos = eliminar_datos_usuario(datos)

   # Categoría del usuario
   categoria_usuario(datos)
   

3. *Gestión de Servicios y Productos*:
   python
   # Crear servicio
   datos_servicios = generar_servicio(datos_servicios)

   # Listar servicios
   listar_servicios(datos_servicios)

   # Actualizar servicio
   datos_servicios = actualizar_servicio(datos_servicios)

   # Eliminar servicio
   datos_servicios = eliminar_servicio(datos_servicios)

   # Crear producto
   datos_servicios = generar_producto(datos_servicios)

   # Listar productos
   listar_productos(datos_servicios)

   # Actualizar producto
   datos_servicios = actualizar_producto(datos_servicios)

   # Eliminar producto
   datos_servicios = eliminar_producto(datos_servicios)
   

4. *Gestión de Ventas*:
   python
   # Ver registro de ventas totales
   ventas_totales(datos)

   # Registrar la compra de un servicio
   datos_ventas = interacciones_servicios(datos_ventas)

   # Registrar la compra de un producto
   datos_ventas = interacciones_productos(datos_ventas)
   

5. *Guardar cambios*:
   python
   guardar_datos_servicios(datos, RUTA_CENTRAL)
   guardar_datos_ventas(datos_ventas, RUTA_DE_VENTAS)
   
