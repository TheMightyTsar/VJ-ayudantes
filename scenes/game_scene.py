import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.player import Player

from elements.enemy import Enemy



def gameloop():
    ''' iniciamos los modulos de pygame'''

    pygame.init()

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700

    # crear el objeto pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("assets/pixelBackground.jpg").convert()

    ''' 2.- generador de enemigos'''
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    clock = pygame.time.Clock()

    # variable booleana para manejar el loop
    running = True

    # loop principal del juego

    while running:

        screen.blit(background_image, [0, 0])
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

            # es un evento que agrega enemigos?
            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # dibujamos todos los sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # vemos si algun enemigo a chocado con el jugador
        if pygame.sprite.spritecollideany(player, enemies):
            # si pasa, removemos al jugador y detenemos el loop del juego
            player.kill()
            running = False

        # actualizamos la interfaz



        # obtenemos todas las teclas presionadas actualmente
        pressed_keys = pygame.key.get_pressed()

        # actualizamos el sprite del jugador basado en las teclas presionadas
        player.update(pressed_keys)

        # actualizamos los enemigos
        enemies.update()

        pygame.display.flip()

        clock.tick(30)