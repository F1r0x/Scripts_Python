#!/usr/bin/env python3

# Juegos
juegos = {
    "Super Mario Bros",
    "Zelda: Breath of the Wild",
    "Cyberpunk 2077",
    "Final Fantasy VII"
}

tope = 500

# Géneros
genero = {
    "Super Mario Bros": "Aventura",
    "Zelda: Breath of the Wild": "Aventura",
    "Cyberpunk 2077": "Rol",
    "Final Fantasy VII": "Rol"
}

# Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros": (400, 200),
    "Zelda: Breath of the Wild": (600, 20),
    "Cyberpunk 2077": (60, 120),
    "Final Fantasy VII": (924, 3) 
}

# Clietes
clientes = {
    "Super Mario Bros": {"Juan", "Paco", "Albert", "Lucia", "Lola"},
    "Zelda: Breath of the Wild": {"Marcos", "Paco", "Albert", "Juana", "Rafa"},
    "Cyberpunk 2077": {"Juan", "Paco", "Albert", "Lucia", "Lola"},
    "Final Fantasy VII": {"Roberto", "Paco", "Juana", "Lucia", "Elia"}
}

def sumario(juego):
    # Sumario
    print(f"-----------------------------------------")
    print(f"\n[i] Resumen del juego {juego}\n")
    print(f"[+] Genero del juego: {genero[juego]}")
    print(f"[+] Total de ventas de este juego: {ventas_y_stock[juego][0]} unidades.")
    print(f"[+] Total de stock para este juego: {ventas_y_stock[juego][1]} unidades.")
    print(f"[+] Clientes que han adquirido el juego: {clientes[juego]}")

for juego in juegos:
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)

ventas_totales = lambda: sum(
    ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope)

print(f"\nEl total de ventas de todos los productos ha sido de {ventas_totales()} productos.")
