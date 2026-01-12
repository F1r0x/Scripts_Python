#!/usr/bin/env python3

# Clase Calculadora
class Calculadora:

    def __init__(valor1, valor2):
       valor1 = valor1
       valor2 = valor2


    # Suma
    def suma(valor1, valor2):
        return valor1 + valor2

    def resta(valor1, valor2):
        return valor1 - valor2
    
    def mult(valor1, valor2):
        return valor1 * valor2
    
    def div(valor1, valor2):
        return valor1 / valor2 if valor2 != 0 else f"\n[!] Error: No se puede dividir entre 0"


calc = print(Calculadora.suma(4, 5))
calc = print(Calculadora.resta(4, 5))
calc = print(Calculadora.mult(4, 5))
calc = print(Calculadora.div(4, 5))
calc = print(Calculadora.div(4, 0))