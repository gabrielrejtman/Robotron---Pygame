import random
from config import *


class Mine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.assets = pygame.transform.scale(pygame.image.load('sprites/Enemys/Mina/red.png'), (32, 42))
        self.image = self.assets
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
