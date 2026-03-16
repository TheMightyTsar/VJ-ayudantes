import pygame
import random
from pygame.locals import (RLEACCEL)

BUGpng = pygame.image.load('assets/bug.png')
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.surf = BUGpng_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # la posicion inicial es generada
        # aleatoriamente, al igual que la velocidad
        self.rect = self.surf.get_rect(
            center=(
                screen.get_width() + 100,
                random.randint(0, screen.get_height()),
            )
        )
        self.speed = random.randint(3, 5)


    def update(self):
        # POR HACER (2.5): Mover a los enemigos

        # POR HACER (2.5): Destruir a los enemigos
        pass

