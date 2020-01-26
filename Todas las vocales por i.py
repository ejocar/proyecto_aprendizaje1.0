
strings_a_sustituir = ["i"]
string_a_cambiar = input("Introduce una palabra: ")

for string in strings_a_sustituir:
    string_a_cambiar = string_a_cambiar.replace("a", string, 10)
    string_a_cambiar = string_a_cambiar.replace("e", string, 10)
    string_a_cambiar = string_a_cambiar.replace("o", string, 10)
    string_a_cambiar = string_a_cambiar.replace("u", string, 10)
    string_a_cambiar = string_a_cambiar.replace("A", string, 10)
    string_a_cambiar = string_a_cambiar.replace("E", string, 10)
    string_a_cambiar = string_a_cambiar.replace("I", string, 10)
    string_a_cambiar = string_a_cambiar.replace("O", string, 10)
    string_a_cambiar = string_a_cambiar.replace("U", string, 10)

print(string_a_cambiar)