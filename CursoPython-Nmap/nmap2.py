#!/usr/bin/env python3

## Importar libreria python-nmap
import nmap

## Creamos un objeto llamado nm
nm = nmap.PortScanner()

## Ejecutamos el escaneo:
# Parámetros utilizados (ip, ports)
# Esto equivale a: nmap -p 1-65535 192.168.68.57
nm.scan("192.168.68.57", "1-65535")

# Comrprueba todos los hosts encontrados, en este
# caso solo está (192.168.68.57).
for host in nm.all_hosts():
    print(f"\n [+] Host: {host}")

    # Recorre todos los protocolos encontrados para este host
    for proto in nm[host].all_protocols():
        print(f"\n [+] Protocol: {proto}\n")

        # Recorre todos los puestos econtrados para ese host y protocolo
        for port in sorted(nm[host][proto]):

            # Obtiene el estado del puerto
            state = nm[host][proto][port]['state']
            # Obtiene el servicio asociado al puerto
            service = nm[host][proto][port]['name']
            # Imprime la información de los puertos.
            print(f" - Puerto {port}: {state} ({service})")
