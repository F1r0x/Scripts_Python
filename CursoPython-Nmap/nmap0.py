#!/usr/bin/env python3

import subprocess

resultado = subprocess.run(
    ["nmap", "--open", "-p-", "-v", "-n", "192.168.68.57"],
    capture_output=True,
    text=True
)

print(resultado.stdout)