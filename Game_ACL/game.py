import pygame
from obstacle import Obstacle
from player import Player
from monster import Monster


class Game:

    def __init__(self, screen_width, screen_height):
        self.is_playing1 = False
        self.is_playing2 = False
        self.pressed = {}
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_obstacles = pygame.sprite.Group()
        self.all_monsters = pygame.sprite.Group()

    def start1(self):
        self.is_playing1 = True
        self.all_players.add(self.player)
        self.all_obstacles.add(Obstacle(self, self.screen_width / 2, self.screen_height / 2))
        self.all_obstacles.add(Obstacle(self, self.screen_width / 2 - 90, self.screen_height / 2 - 80))
        self.all_monsters.add(Monster(self, 4 * self.screen_width / 5, 4 * self.screen_height / 5))

    def start2(self):
        self.player.rect.x = 0
        self.player.rect.y = 0
        self.is_playing2 = True
        self.is_playing1 = False
        self.all_obstacles.add(Obstacle(self, self.screen_width / 5, self.screen_height / 5))
        self.all_obstacles.add(Obstacle(self, self.screen_width / 5 - 90, self.screen_height / 5 - 80))

    def update(self, screen):

        self.all_obstacles.draw(screen)
        self.all_players.draw(screen)
        self.all_monsters.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < self.screen_width:
            self.player.move_right()
            if self.check_collision(self.player, self.all_obstacles):
                self.player.move_left()
            elif self.check_collision(self.player, self.all_monsters):
                self.player.move_left()
                self.is_playing1 = False
                self.is_playing2 = False
                self.player.reset_position()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -5:
            self.player.move_left()
            if self.check_collision(self.player, self.all_obstacles):
                self.player.move_right()
            elif self.check_collision(self.player, self.all_monsters):
                self.player.move_right()
                self.is_playing1 = False
                self.is_playing2 = False
                self.player.reset_position()

        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
            if self.check_collision(self.player, self.all_obstacles):
                self.player.move_down()
            elif self.check_collision(self.player, self.all_monsters):
                self.player.move_down()
                self.is_playing1 = False
                self.is_playing2 = False
                self.player.reset_position()

        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < self.screen_height - 5:
            self.player.move_down()
            if self.check_collision(self.player, self.all_obstacles):
                self.player.move_up()
            elif self.check_collision(self.player, self.all_monsters):
                self.player.move_up()
                self.is_playing1 = False
                self.is_playing2 = False
                self.player.reset_position()

    def check_collision(self, sprite, group):

        """
        collision = False
        for element in group:
            if sprite.rect.colliderect(element.rect):
                collision = True
        return collision
        """

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

