
numeros_usuario = []
numero_del_usuario = ""
n_numeros = int(input("¿Cuántos números desea introducir?: "))

while len(numeros_usuario) < n_numeros:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Número añadido")

print("La media de los números es: {}".format(int(sum(numeros_usuario)/n_numeros)))