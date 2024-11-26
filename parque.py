'''El costo de entrada a un parque de diversiones depende de la edad de las personas; 
si la persona tiene más de 1 año y menos de 4 años entra gratis; si tiene entre 4 y 8 
años paga US $2, si tiene entre 9 y 16 años paga US $5, si tiene entre 17 y 
35 años paga US $6 y si tiene más de 35 años paga US$10. Imprimir el valor en dólares 
y pesos colombianos. '''

edad=int(input("Ingrese su edad: "))
if edad>=1 and edad<=4:
     print("La entrada es gratis")
elif edad>=4 and edad<=8:
     print("La entrada cuesta US $2 ,  COP 8.777 ")
elif edad>=9 and edad<=16:
     print("La entrada cuesta US $5 ,  COP 21.942 ")
elif edad>=17 and edad<=35:
     print("La entrada cuesta US $6 ,  COP 26.331 ")
elif edad>=35:
     print("La entrada cueesta US $10 , COP 43.885")
