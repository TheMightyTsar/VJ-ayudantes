import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from CarpetaBase.elements.player import Player

from CarpetaBase.elements.enemy import Enemy


""""
Este es el modulo game_scene, aqui se encuentra 
la escena en donde ocurre nuestro juego
"""


def gameloop(screen):
    ''' Definimos el fondo de nuestra escena'''
    # POR HACER: añadir fondo del display
    background_image = None

    ''' Preparamos el gameloop '''
    # POR HACER (2.8): Crear el reloj del juego
    clock = None

    # POR HACER (2.7): Generador de enemigos
    ADDENEMY = None

    # POR HACER (2.6): Creamos la instancia de jugador
    player = None

    # POR HACER (2.6): Creamos los grupos de sprites
    enemies = None
    all_sprites = None

    ''' hora de hacer el gameloop '''
    # variable booleana para manejar el loop
    running = True

    # GAME LOOP: loop principal del juego
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

            # POR HACER (2.7): Generar enemigos

        # POR HACER (2.6): Dibujar los sprites

        # POR HACER (2.6): Actualizar los sprites

        # POR HACER (2.9): Colisiones

        # POR HACER (2.4): Actualizar la ventana con lo dibujado

        # POR HACER (2.8): Controlar la velocidad de fotogramas