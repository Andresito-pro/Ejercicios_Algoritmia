#Nombre: Comprobar año bisiesto
#Entrada:
# año: solicita la entrada de un valor tipo número
# Proceso: 
# if: condiciona que si el número es divisible entre 4 entonces
# else:Significa que va a pasar si no se cumple la función del si
# Salida:
#  imprime el valor si es o no es bisiesto

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")