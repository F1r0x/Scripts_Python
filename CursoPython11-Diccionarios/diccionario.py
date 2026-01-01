#!/usr/bin/env python3

# Diccionario
mi_diccionario = {"nombre": "Juan", "edad": 23, "nacionalidad": "Español"}

print(type(mi_diccionario))
print(len(mi_diccionario))
print(mi_diccionario)
print(mi_diccionario["nombre"])
print(mi_diccionario["edad"])
print(mi_diccionario["nacionalidad"])

#-------------------------------------------------

# Al guardar un nuevo volor sustituye al anterior
mi_diccionario["nombre"] = "Mariano"
print(mi_diccionario)
print(mi_diccionario["nombre"])

#-------------------------------------------------

# Podemos guardar nuevos campos y valores en el diccionario
mi_diccionario["profesion"] = "Desarrollador Web"
print(mi_diccionario)
print(len(mi_diccionario))
print(mi_diccionario["profesion"])
