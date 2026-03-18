import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

def gameloop(screen):

    # definimos nuestro fondo de pantalla

    # inicializamos el reloj de nuestra pantalla
    clock = pygame.time.Clock()

    # variable booleana para manejar el loop
    running = True

    # loop principal de nuestra escena inicial
    while running:
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_ESCAPE:
                    running = False

            # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False

        # hacemos que pasen ticks de tiempo
        clock.tick(30)