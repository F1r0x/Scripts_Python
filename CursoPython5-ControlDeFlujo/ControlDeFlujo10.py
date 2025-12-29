#!/usr/bin/env python3

edad = 18
nacionalidad = "argentino"

if edad >= 18:
    if nacionalidad == "argentino":
        print(" Puedes votar en las elecciones Argentinas.")

if edad >= 18 or nacionalidad != "española":
    print(" Eres menor y puedes votar en las elecciones.")
else:
    print(" No puedes votar en las elecciones.")