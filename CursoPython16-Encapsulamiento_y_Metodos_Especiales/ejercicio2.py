#!/usr/bin/env python3

class Ejemplo:

    # Atributo Privado para ello se utilizan dos barras bajas
    def __init__(self):
        self. __atributo_privado = "Soy una atributo privado y no deberías de poder verme" # name mangling

ejemplo = Ejemplo()
# No lo podemos ver
#print(ejemplo.__atributo_privado)

print(ejemplo._Ejemplo__atributo_privado)