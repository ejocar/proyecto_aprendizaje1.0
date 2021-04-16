
numero1 = input("Introduce un numero: ")
numero2 = input("Introduce otro numero: ")
numero3 = input("Introduce un ultimo numero: ")

if numero1 > numero2 and numero1 > numero3:
    print numero1
elif numero2 > numero1 and numero2 > numero3:
    print numero2
else:
    print numero3