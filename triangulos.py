#Nombre: Determina el tipo de triangulos
# Entrada:
# Se ingresan las longitudes de los tres lados del triángulo (num1, num2, num3)
# Proceso:
# Se evalúa el tipo de triángulo comparando las longitudes de sus lados
# Salida:
# Se imprime el tipo de triángulo (equilátero, isósceles o escaleno)

num1=float(input("Ingrese el lado 1: "))
num2=float(input("Ingrese el lado 2: "))
num3=float(input("Ingrese el lado 3: "))
if num1 == num2 and num2 == num3:
    print("El triangulo es equilatero. ")
elif num1== num2 or num2==num3 or num1==num3:
    print("El triangulo es isocéles")
else:
    print("El triangulo es escaleno")