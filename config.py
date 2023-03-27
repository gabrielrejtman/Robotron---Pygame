import pygame
import pygame
from pygame import mixer
import random as rand
pygame.font.init()
pygame.mixer.init()

# looping
loop = True

# Colors
RED = (134, 28, 9)
YELLOW = (212, 169, 65)
WHITE = (255, 255, 255)
GREEN = (0, 127, 33)
BLUE = (0, 97, 148)
DARKER_GREEN = (31, 61, 12)
DARKER_BLUE = (11, 11, 69)

colour_list = [RED, YELLOW, GREEN, BLUE, DARKER_GREEN]

# screen height and width
screen_width = 1000
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

# Sounds
death = pygame.mixer.Sound("sounds/death.mp3")
get_human = pygame.mixer.Sound("sounds/coleta.mp3")
kill_human = pygame.mixer.Sound("sounds/oin.mp3")
bullet = pygame.mixer.Sound("sounds/tiro.mp3")
    
proportion = 100
num_squares = 50
square_size = 1
# sets the game surface
game_surface = pygame.Surface(([1000, 650]))

border_width = 5

# clock 
clk = pygame.time.Clock()
fps = 60

# player/enemies/bullet speed
player_speed = 7
bullet_speed = 11
shoot_cooldown = 7

# sheets 
player_sheet = pygame.image.load("sprites/playersheet.png")
player = pygame.image.load("sprites/player.png")
bullet = pygame.image.load("sprites/testeball.png")

# font
score_font = pygame.font.Font("font/robotron-2084.ttf", 30)
gam_over_font = pygame.font.Font("font/robotron-2084.ttf", 60)
sbb_font = pygame.font.Font("font/robotron-2084.ttf", 20)
