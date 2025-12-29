#!/usr/bin/env python3

variable = "Soy global"

def mi_funcion():
    variable_local = "Soy local"
    variable = "Soy local"
    print(variable_local)
    print(variable) # La varible solo cambia dentro de la función
mi_funcion()

# Fuera de la función mantiene el valor establecido fuera de la función.
print(variable)