import pygame
import random
from pygame.locals import (RLEACCEL)

BUGpng = pygame.image.load('../assets/bug.png')
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Enemy, self).__init__()
        self.surf = BUGpng_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # la posicion inicial es generada aleatoriamente, al igual que la velocidad
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH + 100,
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(3, 5)

    # el sprite tendra velocidad
    # cuando traspase el lado izq de la pantalla lo eliminamos
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

