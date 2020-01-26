
strings_a_sustituir = ["a", "e", "i", "o", "u"]
string_a_cambiar = input("Introduce una palabra: ")
n_strings = 0

for string in string_a_cambiar:
    if string in strings_a_sustituir:
        n_strings += 1
        string_a_cambiar = string_a_cambiar.replace(string, str(n_strings), 1)

print(string_a_cambiar)