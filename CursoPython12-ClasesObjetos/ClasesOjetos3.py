#!/usr/bin/env python3

class CuentaBancaria:

    def __init__(self, cuenta, nombre, saldo=0): # Con saldo=0 establecemos el valor por defecto a la hora de crear el objeto.
        self.cuenta = cuenta
manolo = CuentaBancaria("12345678", "Manolo Vieira", 1000)