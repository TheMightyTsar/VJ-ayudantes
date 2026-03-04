import scenes.basic_scene as basic_scene
import scenes.game_scene as game_scene
import pygame


pygame.init()

# definimos el tamaño de nuestra pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# creamos el objeto pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# manejamos aqui como funcionaran las escenas de nuestro juego
basic_scene.gameloop(screen)
game_scene.gameloop(screen)
