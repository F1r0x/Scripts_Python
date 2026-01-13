#!/usr/bin/env python3

class Dispositivo:

    def __init__(self, modelo):
        self.modelo = modelo

    def escanear_vulnerabilidades(self):
         raise NotImplementedError("Esté método debe ser definido para el resto de subclases existentes.")

class Ordenador(Dispositivo):
        def escanear_vulnerabilidades(self):
            return f"\n [+] Aálisis de vulnerabilidades concluido: Actulización de software necesaria, múltiples descactulizaciones de software detectadas."

class Router(Dispositivo):
        def escanear_vulnerabilidades(self):
            return f"\n [+] Aálisis de vulnerabilidades concluido: Múltiples puertos críticos detectados como abiertos, es recomendable cerrar estos puertos."

class TelefonoMOvil(Dispositivo):
        def escanear_vulnerabilidades(self):
            return f"\n [+] Aálisis de vulnerabilidades concluido: Múltiples aplicaciones detectadas con permisos excesivos."


def realizar_escaneo(dispositivo):
     print(dispositivo.escanear_vulnerabilidades())

ordenador = Ordenador("Dell XPS")
router = Router("Tp-Link Archer 50")
movil = TelefonoMOvil("Iphon 17 Pro")


realizar_escaneo(ordenador)
realizar_escaneo(router)
realizar_escaneo(movil)