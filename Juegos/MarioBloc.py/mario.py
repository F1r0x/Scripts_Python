#!/usr/bin/env python3

import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi primer juego")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,255,255), (375, 275, 50, 50))  # Cuadrado
    pygame.display.flip()

pygame.quit()
