from config import *
from layouts import Layouts
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, ang):
        pygame.sprite.Sprite.__init__(self)
        self.ang = ang
        self.speed = bullet_speed
        self.image = pygame.transform.scale(bullet, (150, 15))

        if self.ang[0] == 0:
            self.image = pygame.transform.rotate(self.image, 90)

        elif self.ang[0] == 1 and self.ang[1] == -1:
            self.image = pygame.transform.rotate(self.image, 45)

        elif self.ang[0] == -1 and self.ang[1] == -1:
            self.image = pygame.transform.rotate(self.image, 135)

        elif self.ang[0] == -1 and self.ang[1] == 1:
            self.image = pygame.transform.rotate(self.image, 225)

        elif self.ang[0] == 1 and self.ang[1] == 1:
            self.image = pygame.transform.rotate(self.image, 315)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += self.speed * self.ang[0]
        self.rect.y += self.speed * self.ang[1]
