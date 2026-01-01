#!/usr/bin/env python3

import pygame
import sys

# Inicializar pygame
pygame.init()

# Tamaño de la ventana
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake - Paso 1")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)

# Serpiente (solo la cabeza)
x = 300
y = 200
tam = 20
vel = 20

# Dirección
dx = 0
dy = 0

# Reloj
reloj = pygame.time.Clock()

# Bucle principal
while True:
    reloj.tick(10)  # velocidad del juego

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                dx = 0
                dy = -vel
            if evento.key == pygame.K_DOWN:
                dx = 0
                dy = vel
            if evento.key == pygame.K_LEFT:
                dx = -vel
                dy = 0
            if evento.key == pygame.K_RIGHT:
                dx = vel
                dy = 0

    # Mover serpiente
    x += dx
    y += dy

    # Dibujar
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, VERDE, (x, y, tam, tam))
    pygame.display.update()
