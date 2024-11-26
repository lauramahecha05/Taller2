'''Desarrolle un algoritmo que ingrese dos números y luego los imprima de forma 
ascendente.(primero se imprime el menor y luego el mayor)'''

numero1= int(input("Ingrese el primer numero: "))
numero2= int(input("Ingrese el segundo numero: "))

if numero1 < numero2:
  print(f"Los numeros en forma ascendente: {numero1},{numero2}")
else:
  print(f"Los numeros en forma ascendente:{numero2},{numero1}")
  
