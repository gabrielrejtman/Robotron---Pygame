import pygame

from config import *
from random import randint


class Red(pygame.sprite.Sprite):
    def __init__(self, x, y, player_positions):
        super().__init__()
        self.x = x
        self.y = y
        self.enemy_vel = 1
        self.hit_box = (self.x, self.y, 34, 34)
        self.assets = []
        self.assets.append(pygame.transform.scale(pygame.image.load('sprites/Enemys/Vermelho/static.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Vermelho/left_feet_raised.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load('sprites/Enemys/Vermelho/static.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Vermelho/right_feet_raised.png'), (32, 42)))
        self.assets.append(pygame.transform.scale(pygame.image.load('sprites/Enemys/Vermelho/static.png'), (32, 42)))
        self.current_sprite = 0
        self.image = self.assets[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.moving_x = False
        self.moving_y = False
        self.player = player_positions

    def move_x(self, right=True):
        if right:
            self.rect.x += self.enemy_vel
        else:
            self.rect.x -= self.enemy_vel
        self.moving_x = True

    def move_y(self, above=True):
        if above:
            self.rect.y += self.enemy_vel
        else:
            self.rect.y -= self.enemy_vel
        self.moving_y = True

    def enemy_movement(self):
        self.moving_x = False
        self.moving_y = False

        if self.player.y >= self.rect.y - 30:
            self.move_y(above=True)
        if self.player.y <= self.rect.y:
            self.move_y(above=False)
        if self.player.x >= self.rect.x - 60:
            self.move_x(right=True)
        if self.player.x <= self.rect.x - 50:
            self.move_x(right=False)

        if self.current_sprite >= 4:
            self.current_sprite = 0
        else:
            self.current_sprite += 0.05

        self.image = self.assets[int(self.current_sprite)]

    def update(self):
        self.enemy_movement()


class Green(pygame.sprite.Sprite):
    def __init__(self, x, y, player_positions):
        super().__init__()
        self.x = x
        self.y = y
        self.enemy_vel_x = 1
        self.enemy_vel_y = 1
        self.hit_box = (self.x, self.y, 34, 34)
        self.assets_front = []
        self.assets_left = []
        self.assets_right = []

        self.assets_front.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/front.png'), (32, 42)))
        self.assets_front.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/walking/front_1.png'), (32, 42)))
        self.assets_front.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/front.png'), (32, 42)))
        self.assets_front.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/walking/front_2.png'), (32, 42)))
        self.assets_front.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/front.png'), (32, 42)))

        self.assets_left.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/left.png'), (32, 42)))
        self.assets_left.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/walking/left_1.png'), (32, 42)))
        self.assets_left.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/left.png'), (32, 42)))
        self.assets_left.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/walking/left_2.png'), (32, 42)))
        self.assets_left.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/left.png'), (32, 42)))

        self.assets_right.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/right.png'), (32, 42)))
        self.assets_right.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/walking/right_1.png'), (32, 42)))
        self.assets_right.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/right.png'), (32, 42)))
        self.assets_right.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/walking/right_2.png'), (32, 42)))
        self.assets_right.append(pygame.transform.scale(pygame.image.load(
            'sprites/Enemys/Verdão/static/right.png'), (32, 42)))

        self.sprite_state = 0
        self.current_sprite = 0
        self.image = self.assets_front[self.sprite_state]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.moving_x = randint(0, 1)
        self.moving_y = randint(0, 1)

        if not self.moving_x and not self.moving_y:
            self.moving_x = 1
        self.player = player_positions
        self.max = randint(100, 110)
        self.spawn = (x, y)

    def get_enemy_vel_x(self):
        return self.enemy_vel_x

    def get_enemy_vel_y(self):
        return self.enemy_vel_y

    def enemy_movement(self):

        if self.moving_x:

            self.rect.x += self.enemy_vel_x

            if self.rect.x == self.spawn[0] + self.max:
                self.enemy_vel_x = - self.enemy_vel_x
                self.moving_x = False
                self.moving_y = True

            elif self.rect.x == self.spawn[0] - self.max:
                self.enemy_vel_x = - self.enemy_vel_x
                self.moving_x = False
                self.moving_y = True

        elif self.moving_y:

            self.rect.y -= self.enemy_vel_y

            if self.rect.y == self.spawn[1] + self.max:
                self.enemy_vel_y = -self.enemy_vel_y
                self.moving_y = False
                self.moving_x = True

            elif self.rect.y == self.spawn[1] - self.max:
                self.enemy_vel_y = - self.enemy_vel_y
                self.moving_y = False
                self.moving_x = True

        if self.current_sprite >= 4:
            self.current_sprite = 0
        else:
            self.current_sprite += 0.05

        if self.sprite_state == 0:
            self.image = self.assets_front[int(self.current_sprite)]
        elif self.sprite_state == 1:
            self.image = self.assets_left[int(self.current_sprite)]
        else:
            self.image = self.assets_right[int(self.current_sprite)]

    def update(self):
        self.enemy_movement()
