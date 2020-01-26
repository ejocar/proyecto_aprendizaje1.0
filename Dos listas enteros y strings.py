
lista = [1, 2, 3, "hola", "mundo", "hola"]
lista_enteros = []
lista_strings = []

for numero in lista:
    numero = str(numero)
    if numero.isdigit():
        lista_enteros.append(numero)
    else:
        lista_strings.append(numero)

print("Esta es la lista de los enteros: {}".format(lista_enteros))
print("Esta es la lista de los strings: {}".format(lista_strings))