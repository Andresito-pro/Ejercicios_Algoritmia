#Nombre: Comprobar si un número es multiplo de 5
#Entrada:
# Solicitar al usuario que ingrese un número
# Proceso:
# Verificar si el número es múltiplo de 5 usando el operador módulo (%)
# Salida:
# Mostrar un mensaje indicando si el número es múltiplo de 5 o no
num1 = float(input("Ingrese un número: "))

if num1 % 5 == 0:
    print("El número es multiplo de 5")
else: 
    print("El numero NO es multiplo de 5")