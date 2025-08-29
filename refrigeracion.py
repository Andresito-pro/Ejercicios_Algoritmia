#Nombre: Comprobar la temperatura
# Entrada:
# se recibe un dato del usuario (temperatura)
# Proceso:
# se evalúa si la temperatura es mayor o igual a cero
# Salida:
# se muestra que está congelado si la temperatura es menor a 0

num1 = float(input("Ingrese la temperatura: "))
if num1>= 0:
    print("Esta  descongelado")
else:
    print("Esta congelado")