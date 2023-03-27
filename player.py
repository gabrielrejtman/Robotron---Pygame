from config import *
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, sprite):
        super().__init__()
        self.ang_y = 0
        self.ang_x = 1
        self.score = 0
        self.wave_number = 1
        self.shoot_cooldown = shoot_cooldown
        self.bullet_list = []
        self.bullet_group = pygame.sprite.Group()
        self.image = pygame.transform.scale(sprite, (100, 80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])
        self.x = pos[0]
        self.y = pos[1]
        self.direction_player = 1

    def move(self):
        # sets the movement keys to get pressed
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            if not (key[pygame.K_w] or key[pygame.K_s]):
                self.ang_y = 0
            self.rect.x += -self.speed
            self.x = self.rect.x
            self.ang_x = -1

        if key[pygame.K_d]:
            if not (key[pygame.K_w] or key[pygame.K_s]):
                self.ang_y = 0
            self.rect.x += self.speed
            self.x = self.rect.x
            self.ang_x = 1

        if key[pygame.K_w]:
            if not (key[pygame.K_d] or key[pygame.K_a]):
                self.ang_x = 0
            self.ang_y = -1
            self.rect.y += -self.speed
            self.y = self.rect.y

        if key[pygame.K_s]:
            if not (key[pygame.K_d] or key[pygame.K_a]):
                self.ang_x = 0
            self.ang_y = 1
            self.rect.y += self.speed
            self.y = self.rect.y

    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = shoot_cooldown
            bullet = Bullet(self.rect.centerx + (0.15 * self.rect.size[0]*self.direction_player),
                            self.rect.centery, [self.ang_x, self.ang_y])
            self.bullet_group.add(bullet)
            self.bullet_list.append(bullet)
            mixer.music.load('sounds/tiro.mp3')
            mixer.music.play()

    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
