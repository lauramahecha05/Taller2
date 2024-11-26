'''En las pruebas de ICFES, se presentan dos tipos de prueba: Una de aptitud 
matemática y otra de lenguaje. Leer los puntajes obtenidos por un estudiante en 
cada prueba e imprimir en cual obtuvo mayor puntaje. Tenga en cuenta que ambos 
puntajes podrían ser iguales. '''

puntaje_matematicas=float(input("Ingrese el puntaje de matematicas: "))
puntaje_lenguaje=float(input("Ingrese el puntaje de lenguaje: "))

if puntaje_matematicas > puntaje_lenguaje:
    print("El estudiante obtuvo un mayor puntaje en la prueba de matematicas")
if puntaje_lenguaje > puntaje_matematicas:
    print("El estudiante obtuvo un mayor puntaje en la prueba de lenguaje")
else:
    print("El estudiante obtuvo el mismo puntaje en ambas pruebas")

