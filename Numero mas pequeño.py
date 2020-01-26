
numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) <5:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Número añadido")

numero_mas_pequeño = numeros_usuario[0]

for numero in numero_del_usuario:
    if numero < numero_mas_pequeño:
        numero_mas_pequeño = numero

print("El número más pequeño es {}".format(numero_mas_pequeño))