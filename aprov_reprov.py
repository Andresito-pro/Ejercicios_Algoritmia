#Nombre:Saber si abrobó o reprobó
#Entrada:
# num1: solicita la entrada de la nota como un valor numérico 
#Proceso:
# if y else: condicionan el que pasaría si el número cumple o no las condiciones
#Salida:
# se imprime en la terminal si el estudiante aprobó o reprobó

num1 = float(input("Ingrese la nota: "))
if num1 >= 60:
    print("El estudiante aprobo")
else:
    print("El estudiante reprobo")