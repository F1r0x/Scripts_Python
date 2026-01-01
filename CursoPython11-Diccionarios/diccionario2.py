#!/usr/bin/env python3

mi_diccionario = {"nombre": "Juan", "edad": 23, "nacionalidad": "Español"}

if "nombres" in mi_diccionario:
    print(f"\nEsta clave existe en el diccionario.\n")
else:
    print(f"\nEsta clave NO existe en el diccionario.\n")


#---------------------------

# Iterar por cada campo del diccionario
for key, value in mi_diccionario.items():
    print(f"Para la clave [{key}] tendríamos el valor [{value}]")


#----------------------------

print(f"\n[+] Longitud del diccionario: {len(mi_diccionario)}")

# Limpiar diccionario
mi_diccionario.clear()
print(f"\n[+] Longitud del diccionario: {len(mi_diccionario)}")
