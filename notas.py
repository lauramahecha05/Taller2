'''Desarrolle un algoritmo que permita leer una nota 
entre 0.0y 5.0. Imprimir su nota cualitativa equivalente. 
Teniendo en cuenta la siguiente tabla.'''

nota=float(input("Ingrese la nota (entre 0.0 y 5.0): "))
if 4.6 <= nota < 5.0:
    print("Nota cualitativa: Exelente")
elif 3.6 <= nota < 4.6:
    print("Nota cualitativa: Buena")
elif 3.0 <= nota < 3.6:
    print("Nota cualitativa: Aceptable")
elif 2.0 <= nota < 3.0:
    print("Nota cualitativa: Insuficiente")
elif 2.0 <= nota < 0.0:
    print("Nota cualitativa: Deficiente")
else:
    print("Error la nota ingresada esta fuera del rango permitido (0.0 - 5.0).")