
numero_tabla = int(input("De que número quieres la tabla de multiplicar: "))

for multiplo in range(1, 6):
    print("{} x {} = {}".format(numero_tabla, multiplo*2, numero_tabla*multiplo*2))