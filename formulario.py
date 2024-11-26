'''Elabore un algoritmo que lea el nombre, la edad, el sexo (F: Femenino, M: masculino)
 y el estado civil(1:Casado,2:soltero,3:Separado,4: otro) de una persona que desea
   participar en las elecciones este año. Si es menor de edad imprimir mensaje que diga 
   que no puede votar, de lo contrario imprimir el mensaje indicado la mesa en la cual 
   le corresponde votar. '''

nombre=input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))
sexo= input("Ingrese su sexo (F: Femenino, M: Masculino):")
sexo1=sexo.upper()
estado_civil= int(input("Ingrese su estado civil (1: Casado, 2: Soltero, 3: Separado, 4: Otro)"))
if edad < 18:
    print("No puede votar, es menor de edad.")
elif sexo1=="F" and estado_civil==1:
    print ("Señor/a {nombre} Vota en la mesa 1")
elif sexo1=="F" and estado_civil==2:
    print (f"Señor/a {nombre} Vota en la mesa 2")
elif sexo1=="F" and estado_civil==3:
    print (f"Señor/a {nombre} Vota en la mesa 3")
elif sexo1=="F" and estado_civil==4:
    print (f"Señor/a {nombre} Vota en la mesa 4")
elif sexo1=="M" and estado_civil==2:
    print (f"Señor/a {nombre} Vota en la mesa 2")
elif sexo1=="M" and estado_civil==3:
    print (f"Señor/a {nombre} Vota en la mesa 3")
elif sexo1=="M" and estado_civil==4:
    print (f"Señor/a {nombre} Vota en la mesa 4")
