
numero_tabla = int(input("De que número quieres la tabla de multiplicar: "))

for multiplo in range(10, 1, -1):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla*multiplo))