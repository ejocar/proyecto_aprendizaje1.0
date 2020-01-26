
numeros_usuario = []
numero_del_usuario = input("Dime un número: ")
n_numeros = 0

while numero_del_usuario != "fin":
    numeros_usuario.append(numero_del_usuario)
    numero_del_usuario = input("Dime un número: ")
else:
    for numero in numeros_usuario:
        if numero in numeros_usuario:
            n_numeros += 1

print("El número de números es {}".format(n_numeros))