#!/usr/bin/env python3

class CuentaBancaria:
    def __init__(self, cuenta, nombre, dinero=0):

        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero

    def depositar_dinero(self, dinero): # CuentaBancaria.depositar_dinero()

        self.dinero += dinero  # Es lo mismo que (self.dinero = self.dinero + dinero)
        return f"\n[+] Se han depositado {dinero}€, actualmente el balnce de la cuenta es de {self.dinero}€"

    def retirar_dinero(self, dinero):

        if dinero > self.dinero:
            return f"\n[!] Operación denegada: Fondos Insuficientes\n"
    
        self.dinero -= dinero # self.dinero = self.dinero - dinero
        return f"\n[-] Se han retirado -{dinero}€, actualmente el balnce de la cuenta es de {self.dinero}€"


manolo = CuentaBancaria("187263", "Manolo Vieira", 1000)
juan = CuentaBancaria("456534", "Juan Palomo", 4000)

print(f"\n[+] Manolo tiene actualmente: {manolo.dinero}€")
print(manolo.depositar_dinero(500))
print(manolo.depositar_dinero(700))

print(f"\n[+] Manolo tiene actualmente: {manolo.dinero}€")
print(manolo.retirar_dinero(300))
print(manolo.retirar_dinero(900))

print(f"\n[+] Manolo tiene actualmente: {manolo.dinero}€")
print(manolo.retirar_dinero(1300))

print(f"\n[+] Juan tiene actualmente: {juan.dinero}€")

