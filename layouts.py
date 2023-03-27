import wall
from random import *
from config import *


# layouts class 
class Layouts:
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.wall_color = choice(colour_list)
        self.borders()


    def get_group(self):
        return self.group
    
    def borders(self):
        self.group.add(wall.Wall(self.wall_color, (910, 10), (45, 45)))
        self.group.add(wall.Wall(self.wall_color, (910, 10), (45, 600)))
        self.group.add(wall.Wall(self.wall_color, (10, 555), (45, 45)))
        self.group.add(wall.Wall(self.wall_color, (10, 565), (950, 45)))
    
    
        
    