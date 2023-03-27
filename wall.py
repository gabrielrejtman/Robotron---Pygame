import pygame

# walls class 
class Wall(pygame.sprite.Sprite):
    def __init__(self, color, dimensions, coordinates):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = coordinates)

