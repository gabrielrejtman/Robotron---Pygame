from random import *
from config import *
from enemy import *
from player import Player
from layouts import Layouts
from humans import Humans
from obstacles import Mine

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#    joystick.init()


class Game(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.loop = loop
        self.walls = Layouts().get_group()
        self.player_sprites = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.human_group = pygame.sprite.Group()
        self.objects_group = pygame.sprite.Group()
        self.player = Player((500, 300), player)
        self.player_sprites.add(self.player)
        self.background = game_surface
        self.humans_number = 3
        self.add_groups()
        self.gameplay_loop = True
        self.score_text_rect = (150, 15)
        self.game_over_text_rect = (screen_width / 2 - 170, screen_height / 2 - 70)
        self.subtitle_rect = (screen_width / 2 - 270, screen_height / 2 + 40)
        self.wave_number_rect = (415, 615)

    def add_groups(self):
        for i in range(randint(1, 10)):
            enemy_red = Red(randint(75, 865), randint(80, screen_height - 80), self.player)
            enemy_green = Green(randint(140, 800), randint(160, screen_height - 190), self.player)
            self.enemy_group.add(enemy_red)
            self.enemy_group.add(enemy_green)

        for h in range(3):
            human = Humans(randint(75, 865), randint(80, screen_height - 80))
            self.human_group.add(human)

        for i in range(5):
            i = Mine(randint(75, 865), randint(80, screen_height - 80))
            self.objects_group.add(i)

    def add_player(self):
        self.player_sprites.add(self.player)

    # Check if an event happens
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.player.shoot()

    def check_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.gameplay_loop = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                self.add_groups()
                self.add_player()

    # sets the collision between bullet and wall groups
    def bullet_collision(self):
        for wall in self.walls:
            for bullet in self.player.bullet_group:
                if pygame.sprite.collide_mask(bullet, wall):
                    bullet.kill()
        # clear the ball list
        self.player.bullet_list.clear()

    def clear_all(self):
        self.player_sprites.empty()
        self.enemy_group.empty()
        self.human_group.empty()
        self.humans_number = 3

    # sets the collision between player/wall/enemies groups
    def player_collision(self):
        for wall in self.walls:
            for player in self.player_sprites:
                if pygame.sprite.collide_mask(player, wall):
                    if abs(player.rect.top - wall.rect.bottom) < 50:
                        player.rect.y += player_speed
                    elif abs(wall.rect.top - player.rect.bottom) < 50:
                        player.rect.y -= player_speed
                    elif abs(wall.rect.left - player.rect.right) < 50:
                        player.rect.x -= player_speed
                    elif abs(player.rect.left - wall.rect.right) < 50:
                        player.rect.x += player_speed

    def player_damage(self):
        for enemy in self.enemy_group:
            for player in self.player_sprites:
                if pygame.sprite.collide_mask(enemy, player):
                    player.kill()
                    self.gameplay_loop = False
                    self.clear_all()

    def next_level(self):
        if self.humans_number == 0:
            self.player.wave_number += 1
            self.enemy_group.empty()
            self.human_group.empty()
            self.add_groups()
            self.humans_number = 3

    def player_damage_object(self):
        for objects in self.objects_group:
            for player in self.player_sprites:
                if pygame.sprite.collide_mask(objects, player):
                    player.kill()
                    objects.kill()
                    self.player.bullet_group.empty()
                    self.player.bullet_list.clear()
                    self.gameplay_loop = False

    def enemy_damage(self):
        for enemy in self.enemy_group:
            for bullet in self.player.bullet_group:
                if pygame.sprite.collide_mask(enemy, bullet):
                    bullet.kill()
                    enemy.kill()
                    death.play()
                    self.player.score += 100

    def enemy_collision_objects(self):
        for enemy in self.enemy_group:
            for objects in self.objects_group:
                if pygame.sprite.collide_mask(enemy, objects):
                    objects.kill()
                    enemy.kill()
                    death.play()
                    self.player.score += 100

    def collect_humans(self):
        for human in self.human_group:
            for player in self.player_sprites:
                if pygame.sprite.collide_mask(player, human):
                    human.kill()
                    get_human.play()
                    self.player.score += 2000
                    self.humans_number -= 1

    def kill_humans(self):
        for human in self.human_group:
            for enemy in self.enemy_group:
                if pygame.sprite.collide_mask(enemy, human):
                    human.kill()
                    self.humans_number -= 1
                    kill_human.play()

    @staticmethod
    def draw_squares(screen, screen_width, screen_height, num_squares, square_size):
        for i in range(num_squares):
            # Randomly generate the position and color of the square
            x = rand.randint(0, screen_width - square_size)
            y = rand.randint(0, screen_height - square_size)
            color = (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))

            # Draw the square on the screen
            pygame.draw.rect(screen, color, (x, y, square_size, square_size))

    def draw_borders(self):
        colour = choice(colour_list)
        pygame.draw.rect(self.screen, colour, (45, 45, 910, 10))
        pygame.draw.rect(self.screen, colour, (45, 600, 910, 10))
        pygame.draw.rect(self.screen, colour, (45, 45, 10, 555))
        pygame.draw.rect(self.screen, colour, (950, 45, 10, 565))

    # sets the game looping
    def game_loop(self):
        while self.loop:
            self.screen.blit(game_surface, (0, 0))
            if self.gameplay_loop:
                self.check_events()
                self.draw_sprites()
                self.player.move()
                self.player_collision()
                self.player_damage()
                self.bullet_collision()
                self.enemy_damage()
                self.collect_humans()
                self.kill_humans()
                self.check_points()
                self.human_collide()
                self.enemy_collision_objects()
                self.player_damage_object()
                self.draw_squares(screen, screen_width, screen_height, num_squares, square_size)
                self.draw_borders()
                self.next_level()
            else:
                self.check_events_menu()
                c = choice(colour_list)
                game_over = gam_over_font.render("You Died", True, c)
                game_over_sb = sbb_font.render("Press SPACE to play again or ESC to exit", True, c)
                self.screen.blit(game_over, self.game_over_text_rect)
                self.screen.blit(game_over_sb, self.subtitle_rect)
            pygame.display.update()
            clk.tick(fps)

    # draw elements
    def draw_sprites(self):
        self.walls.update()
        self.player.update()
        self.player_sprites.draw(self.screen)
        self.player.bullet_group.draw(self.screen)
        self.player.bullet_group.update()
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()
        self.human_group.draw(self.screen)
        self.human_group.update()
        self.objects_group.draw(self.screen)

    def check_points(self):
        score_text = score_font.render(str(self.player.score), True, choice(colour_list))
        wave_text = score_font.render(str(self.player.wave_number) + " WAVE", True, choice(colour_list))
        self.screen.blit(score_text, self.score_text_rect)
        self.screen.blit(wave_text, self.wave_number_rect)

    def human_collide(self):
        for wall in self.walls:
            for human in self.human_group:
                if pygame.sprite.collide_mask(human, wall):
                    if abs(human.rect.top - wall.rect.bottom) < 50:
                        human.human_movement(True, False)
                    elif abs(wall.rect.top - human.rect.bottom) < 50:
                        human.human_movement(True, False)
                    elif abs(wall.rect.left - human.rect.right) < 50:
                        human.human_movement(False, True)
                    elif abs(human.rect.left - wall.rect.right) < 50:
                        human.human_movement(False, True)
