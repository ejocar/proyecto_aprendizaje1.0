
frase_del_usuario = input("Introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]

n_vocales = 0

for vocal in frase_del_usuario:
    if vocal in vocales:
        n_vocales += 1

print("El número de vocales es {}".format(n_vocales))