#!/usr/bin/env python3

class Ejemplo:

    # Atributo Personal para ello se utiliza una barra baja
    def __init__(self):
        self. _atributo_protegido = "Soy una atributo protegido y no deberías de poder verme"

ejemplo = Ejemplo()
print(ejemplo._atributo_protegido)