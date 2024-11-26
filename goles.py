'''Calcule el promedio de goles anotados por un jugador en 
cuatro encuentros, solo si la suma de estos es mayor
a 10; de lo contrario imprimir “No se pide determinar el promedio”.'''

partido1= int(input("Ingrese los goles del primer encuentro: "))

partido2= int(input("Ingrese los goles del segundo partido: "))

partido3= int(input("Ingrese los goles del tercer partido: "))

partido4= int(input("Ingrese los goles del cuarto partido: "))

suma_goles = partido1 + partido2 + partido3 + partido4

if suma_goles > 10:
    promedio = suma_goles / 4
    print(f"El promedio de los goles es: {promedio}")
else:
    print("No se puede determinar el promedio")


