
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 45, 78, 32, 12, 98]

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = "Bazinga"

print(numeros)