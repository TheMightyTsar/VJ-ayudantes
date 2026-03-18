import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, screen_width, screen_height):
        super(Bullet, self).__init__()
        #POR HACER (2.0): Aspecto inicial de nuestra bala
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=pos)

        # POR HACER (2.1): Variables requeridas por nuestra bala
        self.speed = 20
        self.direction = direction
        self.screen_width = screen_width
        self.screen_height = screen_height


    def update(self):
        # POR HACER (2.2): Mover la bala y destruirla si se sale
        # Mueve el proyectil en la dirección dada
        # (sacamos el vector direccion del eje X y el Eje Y) (vector unitario ejem ejem)
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)

        # Elimina el proyectil si sale de la pantalla
        if (self.rect.right < 0                                 # se sale por izquierda
                or self.rect.left > self.screen_width           # se sale por derecha
                or self.rect.bottom < 0                         # se sale por arriba
                or self.rect.top > self.screen_height):         # se sale por abajo
            self.kill()