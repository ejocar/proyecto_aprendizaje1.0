
strings_a_sustituir = ["VACA"]
string_a_cambiar = input("Introduce una palabra: ")

for string in strings_a_sustituir:
    string_a_cambiar = string_a_cambiar.replace("A", string, 1)
    string_a_cambiar = string_a_cambiar.replace("a", string, 1)

print(string_a_cambiar)