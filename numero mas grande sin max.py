
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 78, 32, 12, 98]
n_cero = 0

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero > n_cero:
        n_cero = numero

print("El número mas grande de la lista es: {}".format(n_cero))