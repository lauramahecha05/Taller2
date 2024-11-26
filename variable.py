'''Resolver la siguiente ecuación, teniendo en cuenta que 
solo se puede realizar si la variable r es diferente de 2;
 en caso contrario hacer P=1 P=(r-2)3 '''

r=float(input("Ingrese el valor de r: "))
if r==2:
    p=1
else:
    p= (r-2)/(r-2)
print ("El valor de P es",p)