#Nombre: Comprobar el ingreso por medio de la contraseña 
# Entrada:
#  Captura la contraseña ingresada por el usuario
# Proceso: 
# Compara la contraseña ingresada con la contraseña correcta ("password")
# Salida:
# Muestra un mensaje indicando si el acceso fue concedido o denegado

clave1 = str(input("Ingrese su contraseña: "))
if clave1 == "password":
    print("Acceso concedido")
else:
    print("Acceso denegado")