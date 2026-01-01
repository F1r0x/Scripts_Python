#!/usr/bin/nv python3

mi_diccionario = {"nombre": "Juan", "edad": 23, "nacionalidad": "Español"}
mi_diccionario_2 = {"edad": "34", "nacionalidad": "Italiano"}
mi_diccionario_3 = {"sexo": "Varon"}

# Establecer condiciones en caso de que el valor no exista
print(mi_diccionario.get("nombre", "No encontrado"))
print(mi_diccionario_2.get("nombre", "No encontrado"))

#------------------------------------------------------

print(mi_diccionario.get("sexo", "Desconocido"))

# Fusionar/Actualizar diccionarios
mi_diccionario.update(mi_diccionario_3)
print(mi_diccionario)

print(mi_diccionario.get("sexo", "Desconocido"))


