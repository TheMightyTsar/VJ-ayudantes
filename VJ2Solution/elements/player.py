import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL)

from VJ2Solution.elements.bullet import Bullet

JorgePNG = pygame.image.load('assets/JorgeVJ.png')
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80))

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        # nos permite invocar métodos o atributos de Sprite
        super(Player, self).__init__()
        self.surf = JorgePNG_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # POR HACER (2.3): Lista de proyectiles
        self.projectiles = pygame.sprite.Group()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -4)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 4)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(4, 0)


        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

        # POR HACER (2.3): Actualizar las balas
        self.projectiles.update()

    def shoot(self, mouse_pos):
        # POR HACER (2.3): Crear bala y calcular su direccion
        # Calcula la dirección del proyectil
        x_distance = mouse_pos[0] - self.rect.centerx
        y_distance = mouse_pos[1] - self.rect.centery
        length = ((mouse_pos[0] - self.rect.centerx) ** 2 + (mouse_pos[1] - self.rect.centery) ** 2) ** (1 / 2)
        direction = (x_distance / length, y_distance / length)

        projectile = Bullet(self.rect.center, direction, self.screen_width, self.screen_height)
        self.projectiles.add(projectile)
