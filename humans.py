import random
from config import *


class Humans(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.human_vel_x = random.choice([-1, 1])
        self.human_vel_y = random.choice([-1, 1])
        # self.hit_box = (self.x, self.y, 34, 34)
        self.assets = []
        self.assets.append(pygame.transform.scale(pygame.image.load('Assets/Baby.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load('Assets/Mother.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load('Assets/Father.png'), (32, 42)))
        self.current_sprite = random.randint(0, 2)
        self.image = self.assets[self.current_sprite]
        self.flip = False
        if self.human_vel_x == -1:
            self.flip = not self.flip
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.moving_x = False
        self.moving_y = False

    def human_movement(self, collide_x, collide_y):
        if collide_x:
            self.human_vel_y = -self.human_vel_y

        if collide_y:
            self.flip = not self.flip
            self.human_vel_x = -self.human_vel_x

        else:
            self.rect.x += self.human_vel_x
            self.rect.y -= self.human_vel_y
        self.image = self.assets[int(self.current_sprite)]

    def update(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        collide_x = False
        collide_y = False
        self.human_movement(collide_x, collide_y)