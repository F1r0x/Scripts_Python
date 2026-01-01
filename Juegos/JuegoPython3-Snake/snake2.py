#!/usr/bin/env python3

import pygame
import sys

pygame.init()

# Ventana
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake - Paso 2")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)

# Tamaño del bloque
tam = 20
vel = 20

# Serpiente (lista de bloques)
snake = [(300, 200)]  # solo la cabeza al inicio
longitud = 3  # longitud inicial

# Dirección
dx = 0
dy = 0

# Reloj
reloj = pygame.time.Clock()

while True:
    reloj.tick(10)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -vel
            if evento.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = vel
            if evento.key == pygame.K_LEFT and dx == 0:
                dx = -vel
                dy = 0
            if evento.key == pygame.K_RIGHT and dx == 0:
                dx = vel
                dy = 0

    # Mover la cabeza
    x, y = snake[0]
    x += dx
    y += dy
    nueva_cabeza = (x, y)

    # Insertar nueva cabeza al inicio de la lista
    snake.insert(0, nueva_cabeza)

    # Mantener longitud
    if len(snake) > longitud:
        snake.pop()

    # Dibujar
    pantalla.fill(NEGRO)
    for bloque in snake:
        pygame.draw.rect(pantalla, VERDE, (*bloque, tam, tam))
    pygame.display.update()
