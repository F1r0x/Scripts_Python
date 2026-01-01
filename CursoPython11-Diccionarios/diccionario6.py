#!/usr/bin/nv python3

mi_diccionario = {"nombre": "Juan", "edad": 23, "nacionalidad": "Español"}

# Si utilizamos un bucle for sobre el diccionario solo nos
# devolverá las claves sin el valor
print(f"\n[+] Estas son las claves:")
for element in mi_diccionario:
    print(element)

## Respuesta:
# nombre
# edad
# nacionalidad

# Para imprimir los valores podemos utilizar .values()
print(f"\n[+] Estos son los valores:")
for element in mi_diccionario.values():
    print(element)

# Para mostrar los dos utilzaremos .items() y
# usaremos dos variables para el bucle for (key, value)
print(f"\n[+] Estos son los valores y las claves:")
for key, value in mi_diccionario.items():
    print(f"La clave es {key} y el valor {value}")

 