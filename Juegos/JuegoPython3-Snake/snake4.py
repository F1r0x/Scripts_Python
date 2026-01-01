import pygame
import sys
import random

pygame.init()

# Ventana
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake - Borde Toroidal Funcional")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
BLANCO = (255, 255, 255)

# Bloque y velocidad
tam = 20
vel = 20

# Serpiente
snake = [(300, 200)]
longitud = 3
dx, dy = 0, 0

# Comida
def generar_comida():
    x = random.randrange(0, ANCHO // tam) * tam
    y = random.randrange(0, ALTO // tam) * tam
    return (x, y)

comida = generar_comida()

# Puntuación
puntos = 0
fuente = pygame.font.SysFont(None, 36)
fuente_grande = pygame.font.SysFont(None, 48)

# Estado del juego
estado = "jugando"  # "jugando" o "game_over"

# Reloj
reloj = pygame.time.Clock()

while True:
    reloj.tick(10)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN and estado == "game_over":
            # Reiniciar juego
            snake = [(300, 200)]
            longitud = 3
            dx, dy = 0, 0
            puntos = 0
            comida = generar_comida()
            estado = "jugando"

    if estado == "jugando":
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and dy == 0:
            dx, dy = 0, -vel
        if teclas[pygame.K_DOWN] and dy == 0:
            dx, dy = 0, vel
        if teclas[pygame.K_LEFT] and dx == 0:
            dx, dy = -vel, 0
        if teclas[pygame.K_RIGHT] and dx == 0:
            dx, dy = vel, 0

        # --- Movimiento y teletransporte funcional ---
        x, y = snake[0]
        x = (x + dx) % ANCHO
        y = (y + dy) % ALTO
        nueva_cabeza = (x, y)
        snake.insert(0, nueva_cabeza)

        # Comer comida
        if nueva_cabeza == comida:
            longitud += 1
            puntos += 10
            comida = generar_comida()

        # Mantener longitud
        if len(snake) > longitud:
            snake.pop()

        # Colisión consigo misma
        if nueva_cabeza in snake[1:]:
            estado = "game_over"

    # Dibujar
    pantalla.fill(NEGRO)

    if estado == "jugando":
        for bloque in snake:
            pygame.draw.rect(pantalla, VERDE, (*bloque, tam, tam))
        pygame.draw.rect(pantalla, ROJO, (*comida, tam, tam))
        pantalla.blit(fuente.render(f"Puntos: {puntos}", True, BLANCO), (10, 10))
    elif estado == "game_over":
        texto = fuente_grande.render("GAME OVER", True, ROJO)
        texto2 = fuente.render("Presiona cualquier tecla para reiniciar", True, BLANCO)
        pantalla.blit(texto, (80, 150))
        pantalla.blit(texto2, (60, 220))

    pygame.display.update()
