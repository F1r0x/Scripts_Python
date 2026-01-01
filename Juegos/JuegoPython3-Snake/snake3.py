import pygame
import sys
import random

pygame.init()

# Ventana
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake - Paso 3")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
BLANCO = (255, 255, 255)

# Bloque de la serpiente
tam = 20
vel = 20

# Serpiente
snake = [(300, 200)]
longitud = 3

# Dirección
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
                dx, dy = 0, -vel
            if evento.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, vel
            if evento.key == pygame.K_LEFT and dx == 0:
                dx, dy = -vel, 0
            if evento.key == pygame.K_RIGHT and dx == 0:
                dx, dy = vel, 0

    # Mover la cabeza
    x, y = snake[0]
    x += dx
    y += dy
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

    # Dibujar
    pantalla.fill(NEGRO)
    for bloque in snake:
        pygame.draw.rect(pantalla, VERDE, (*bloque, tam, tam))

    pygame.draw.rect(pantalla, ROJO, (*comida, tam, tam))

    # Mostrar puntos
    texto = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    pygame.display.update()
