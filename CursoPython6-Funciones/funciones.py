#!/usr/bin/env python3

def saludo(nombre):
    print(f"\n Hola {nombre}")

saludo("Paco")

#-----------------------------------------------------

def suma(x, y):
    return x + y

resultado = suma(2, 8)
print(f"\n La suma de los dos valores es: {resultado}")

# No es necesario utilizar la variable resultado, podemos pasar los valores
# directamente con la función suma.
print(f"\n La suma de los dos valores es: {suma(9, 5)}")