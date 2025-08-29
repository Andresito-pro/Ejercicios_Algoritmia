#Nombre: Comprobar si un número es positivo o negativo
# Entrada: 
# Solicitar al usuario que ingrese un número
# Proceso:
# Verificar si el número es mayor o igual a cero para determinar si es positivo o negativo
# Salida:
# Mostrar un mensaje indicando si el número es positivo o negativo

num1 = float(input("Ingrese un número: "))
if num1 >= 0: 
    print("El número es positivo")
else:
    print("El número es negativo")