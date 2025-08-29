#Nombre: Identifica si una persona está habilitada para votar 
# Entrada:
# Se ingresan la edad (edad1) y la nacionalidad (nac1) del usuario
# Proceso:
# Se evalúa si la persona es mayor o igual a 18 años y si es colombiana
# Salida:
# Se imprime si la persona puede votar o no

edad1 = float(input("Ingrese su edad: "))
nac1 = input("Ingrese su nacionalidad: ")

if edad1 >= 18 and nac1 == "Colombiano":
    print("Puede votar")  
else:
    print("No puede votar")