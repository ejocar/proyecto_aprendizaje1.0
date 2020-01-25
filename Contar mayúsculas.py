
frase_del_usuario = input("Introduce una frase: ")

mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","X","Y","Z"]

n_mayusculas = 0

for mayuscula in frase_del_usuario:
    if mayuscula in mayusculas:
        n_mayusculas += 1

print("El número de mayúsculas es {}".format(n_mayusculas))