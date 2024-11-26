'''Leer los tres lados del triángulo (A,BY C), imprimir el tipo de triangulo teniendo en
 cuenta que es un triángulo equilátero(solo si sus tres lados son iguales) y 
 es un triángulo escaleno(si todos los lados son diferentes). Además debe validar
   que sus lados permitan formar un triángulo; la condición es que cada lado tiene 
   que ser menos que la suma de los otros dos. '''

A=float(input("Ingrese el valor del lado A del triangulo: "))
B=float(input("Ingrese el valor del lado B del triangulo: "))
C=float(input("Ingrese el valor del lado C del triangulo: "))
if A+B>C and A+C>B and B+C>A:
    if A==B==C:
     print("Es un triangulo equilatero")
    elif A !=B and B != C and C !=A :
       print("Es un triangulo escaleno")
else:
   print("Los lados ingresados no forman un triangulo")
