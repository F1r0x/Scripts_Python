import pygame
import sys

pygame.init()

# Ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Plataformas estilo Mario")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 100, 255)
VERDE = (50, 200, 50)
ROJO = (200, 50, 50)
AMARILLO = (240, 200, 0)

# Fuente
fuente = pygame.font.SysFont(None, 36)
fuente_grande = pygame.font.SysFont(None, 48)

# Jugador
jugador = pygame.Rect(100, 400, 40, 60)
inicio_x = 100
inicio_y = 400
vel_x = 5
vel_y = 0
gravedad = 1
salto = -18
en_suelo = False

# Cámara
offset_x = 0
limite_camara = 400

# Plataformas
plataformas = [
    pygame.Rect(0, 500, 800, 100),
    pygame.Rect(300, 420, 120, 20),
    pygame.Rect(600, 350, 120, 20),
    pygame.Rect(900, 300, 120, 20),
    pygame.Rect(1200, 250, 120, 20),
    pygame.Rect(1600, 500, 800, 100)
]

# Meta
meta = pygame.Rect(1800, 440, 40, 60)

# Monedas
monedas = [
    pygame.Rect(330, 380, 20, 20),
    pygame.Rect(630, 310, 20, 20),
    pygame.Rect(930, 260, 20, 20),
    pygame.Rect(1230, 210, 20, 20),
]

# Puntuación
puntos = 0

# Estado
estado = "inicio"

# Reloj
reloj = pygame.time.Clock()

while True:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if estado == "inicio":
                estado = "jugando"
                puntos = 0
            elif estado in ("fin", "game_over"):
                jugador.x = inicio_x
                jugador.y = inicio_y
                vel_y = 0
                offset_x = 0
                monedas = [
                    pygame.Rect(330, 380, 20, 20),
                    pygame.Rect(630, 310, 20, 20),
                    pygame.Rect(930, 260, 20, 20),
                    pygame.Rect(1230, 210, 20, 20),
                ]
                puntos = 0
                estado = "inicio"

    pantalla.fill(BLANCO)

    # ---------- INICIO ----------
    if estado == "inicio":
        texto = fuente_grande.render("Presiona una tecla para jugar", True, NEGRO)
        pantalla.blit(texto, (120, 250))

    # ---------- JUGANDO ----------
    elif estado == "jugando":
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            jugador.x += vel_x
        if teclas[pygame.K_LEFT] and jugador.x > 0:
            jugador.x -= vel_x

        if jugador.x > limite_camara:
            offset_x += vel_x
            jugador.x = limite_camara

        if teclas[pygame.K_SPACE] and en_suelo:
            vel_y = salto
            en_suelo = False

        vel_y += gravedad
        jugador.y += vel_y

        en_suelo = False
        for plataforma in plataformas:
            plataforma_dib = plataforma.move(-offset_x, 0)
            if jugador.colliderect(plataforma_dib) and vel_y > 0:
                jugador.bottom = plataforma_dib.top
                vel_y = 0
                en_suelo = True

        # Caer al vacío
        if jugador.y > ALTO:
            estado = "game_over"

        # Recoger monedas
        for moneda in monedas[:]:
            if jugador.colliderect(moneda.move(-offset_x, 0)):
                monedas.remove(moneda)
                puntos += 10

        # Llegar a la meta
        if jugador.colliderect(meta.move(-offset_x, 0)):
            estado = "fin"

        # Dibujar
        for plataforma in plataformas:
            pygame.draw.rect(pantalla, VERDE, plataforma.move(-offset_x, 0))

        for moneda in monedas:
            pygame.draw.circle(
                pantalla,
                AMARILLO,
                (moneda.x - offset_x + 10, moneda.y + 10),
                10
            )

        pygame.draw.rect(pantalla, ROJO, meta.move(-offset_x, 0))
        pygame.draw.rect(pantalla, AZUL, jugador)

        texto_puntos = fuente.render(f"Puntos: {puntos}", True, NEGRO)
        pantalla.blit(texto_puntos, (10, 10))

    # ---------- GAME OVER ----------
    elif estado == "game_over":
        texto = fuente_grande.render("GAME OVER", True, ROJO)
        pantalla.blit(texto, (300, 240))

    # ---------- FINAL ----------
    elif estado == "fin":
        texto = fuente_grande.render(f"¡GANASTE! Puntos: {puntos}", True, VERDE)
        pantalla.blit(texto, (220, 240))

    pygame.display.update()
