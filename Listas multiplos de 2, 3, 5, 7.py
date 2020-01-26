
numeros_usuario = []
numero_del_usuario = ""
n_numeros = int(input("¿Cuántos números desea introducir?: "))
lista_dos = []
lista_tres = []
lista_cinco = []
lista_siete = []

while len(numeros_usuario) < n_numeros:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Número añadido")

for indice in range(len(numeros_usuario)):
    numero = numeros_usuario[indice]
    
    if numero % 2 == 0:
        lista_dos += str(numero)

    if numero % 3 == 0:
        lista_tres += str(numero)

    if numero % 5 == 0:
        lista_cinco += str(numero)

    if numero % 7 == 0:
        lista_siete += str(numero)

print("Multiplos de dos: {}".format(lista_dos))
print("Multiplos de tres: {}".format(lista_tres))
print("Multiplos de cinco: {}".format(lista_cinco))
print("Multiplos de siete: {}".format(lista_siete))