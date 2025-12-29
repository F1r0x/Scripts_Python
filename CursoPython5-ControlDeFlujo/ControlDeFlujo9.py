#!/usr/bin/env python3

edad = 18
nacionalidad = "española"

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

if edad < 18 or nacionalidad != "española":
    print("No puedes votar en las elecciones.")
else:
    print("Puedes votar en las elecciones.")