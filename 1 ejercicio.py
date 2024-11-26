'''hacer un programa para un laboratorio de Quimica, que lea un simbolo e
imprimir a que elemento al cual corresponde'''

simbolo=input("Digite el simbolo en mayuscula: ")
simbolo=simbolo.upper()
if simbolo=="H":
    print("El simbolo es Hidrogeno")
elif simbolo=="O":
    print("El elemento es Oxigeno")
elif simbolo=="N":
    print("El elementro es Nitrogeno")
else:
    print("Elemento NO encontrado")



