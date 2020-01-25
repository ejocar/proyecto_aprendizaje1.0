
frase_del_usuario = input("Introduce una frase: ")

espacios = [" "]
puntos = ["."]
comas = [","]

n_espacios = 0
n_puntos = 0
n_comas = 0

for caracter in frase_del_usuario:
    if caracter in espacios:
        n_espacios += 1

for caracter in frase_del_usuario:
    if caracter in puntos:
        n_puntos += 1

for caracter in frase_del_usuario:
    if caracter in comas:
        n_comas += 1

print("El número de espacios es {}".format(n_espacios))
print("El número de puntos es {}".format(n_puntos))
print("El número de comas es {}".format(n_comas))