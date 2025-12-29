#!/usr/bin/env python3

# Variables
name = "Firox"
rol = "Desarrollador Web"
edad = 31

# Llamar a las variables desde el mismo string con {}
print("Hola mi nombre es {name} y soy {rol}")

# Uilizar .format y {} para llamar a las variables
print("Hola soy {}!".format(name))
print("Hola soy {}!".format(rol))

# Podemos generar listas y serán llamadas en orden mediante {}
print("Hola soy {} y tengo {} años.".format(rol,edad))

# Especificar posición de la variable en la lista
print("Hola soy {0}, mi nombre es {1} y adoro ser {0}".format(rol,name))




