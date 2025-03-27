import pygame
from random import randint

# Inicializar pygame
pygame.init()

# Configuración de la ventana
ANCHURA_VENTANA = 600
ALTURA_VENTANA = 600
COLOR_FONDO = (255, 255, 250)
PANTALLA = pygame.display.set_mode((ANCHURA_VENTANA, ALTURA_VENTANA))
pygame.display.set_caption("PRIMER JUEGO")

# Variables del cohete
XX_COHETE = 250
YY_COHETE = 500
MOVIMIENTO_XX_COHETE = 0
VEL_COHETE = 4
ALTURA_COHETE = 88
ANCHURA_COHETE = 175

# Variables de los planetas
ALTURA_PLANETA = 111
ANCHURA_PLANETA = 80
VELOCIDAD_PLANETAS = 2

# Función para generar planetas en posiciones aleatorias
def generar_planeta():
    return randint(30, 150), randint(-200, -50)

XX_PLANETA_IZQUIERDO, YY_PLANETA_IZQUIERDO = generar_planeta()
XX_PLANETA_DERECHO, YY_PLANETA_DERECHO = generar_planeta()
XX_ENTRE_PLANETAS = 350  # Separación entre planetas

# Puntos y marcador
PUNTOS = 0
FUENTE = pygame.font.Font(None, 36)
MARCADOR = FUENTE.render("0 puntos", 1, (255, 0, 0))

# Cargar imágenes
IMG_COHETE = pygame.image.load("img/COHETE.png")
IMG_PLANETA = pygame.image.load("img/PLANETA.png")

# Bucle del juego
PARAR_JUEGO = False
reloj = pygame.time.Clock()

while not PARAR_JUEGO:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PARAR_JUEGO = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                PARAR_JUEGO = True
            if event.key == pygame.K_RIGHT:
                MOVIMIENTO_XX_COHETE = VEL_COHETE
            if event.key == pygame.K_LEFT:
                MOVIMIENTO_XX_COHETE = -VEL_COHETE
        if event.type == pygame.KEYUP:
            MOVIMIENTO_XX_COHETE = 0  # Detener el movimiento al soltar la tecla

    # Mover el cohete dentro de los límites de la pantalla
    XX_COHETE += MOVIMIENTO_XX_COHETE
    XX_COHETE = max(0, min(XX_COHETE, ANCHURA_VENTANA - ANCHURA_COHETE))

    # Mover los planetas hacia abajo
    YY_PLANETA_IZQUIERDO += VELOCIDAD_PLANETAS
    YY_PLANETA_DERECHO += VELOCIDAD_PLANETAS

    # Reiniciar los planetas si salen de la pantalla
    if YY_PLANETA_IZQUIERDO > ALTURA_VENTANA:
        XX_PLANETA_IZQUIERDO, YY_PLANETA_IZQUIERDO = generar_planeta()
        PUNTOS += 1  # Sumar puntos
    if YY_PLANETA_DERECHO > ALTURA_VENTANA:
        XX_PLANETA_DERECHO, YY_PLANETA_DERECHO = generar_planeta()
        PUNTOS += 1

    # Detección de colisiones con ambos planetas
    def colision(XX_PLANETA, YY_PLANETA):
        return (XX_COHETE < XX_PLANETA + ANCHURA_PLANETA and
                XX_COHETE + ANCHURA_COHETE > XX_PLANETA and
                YY_COHETE < YY_PLANETA + ALTURA_PLANETA and
                YY_COHETE + ALTURA_COHETE > YY_PLANETA)

    if colision(XX_PLANETA_IZQUIERDO, YY_PLANETA_IZQUIERDO) or colision(XX_PLANETA_DERECHO + XX_ENTRE_PLANETAS, YY_PLANETA_DERECHO):
        PARAR_JUEGO = True

    # Dibujar elementos en la pantalla
    PANTALLA.fill(COLOR_FONDO)
    PANTALLA.blit(IMG_PLANETA, (XX_PLANETA_IZQUIERDO, YY_PLANETA_IZQUIERDO))
    PANTALLA.blit(IMG_PLANETA, (XX_PLANETA_DERECHO + XX_ENTRE_PLANETAS, YY_PLANETA_DERECHO))
    PANTALLA.blit(IMG_COHETE, (XX_COHETE, YY_COHETE))

    # Mostrar puntos en la pantalla
    MARCADOR = FUENTE.render(f"{PUNTOS} puntos", 1, (255, 0, 0))
    PANTALLA.blit(MARCADOR, (20, 20))

    pygame.display.update()
    reloj.tick(60)  # Mantener 60 FPS

pygame.quit()
