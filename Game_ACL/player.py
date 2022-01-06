import pygame
import game
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.ratio = 15
        self.width = self.game.screen_width/self.ratio
        self.height = self.game.screen_height/self.ratio
        self.health = 80
        self.health_max = 80
        self.attack = 20
        self.velocity = 15
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load(f'assets/pacman_right.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x=20
        self.rect.y=20
        self.game=game

    def change_image(self,direction):
        self.image = pygame.image.load(f'assets/pacman_'+direction+'.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))


    def launch_projectile(self, direction):
        # self.game.sound_manager.play('shoot')
        # creer une nouvelle instance de la classe Projectile
        if direction == 'up':
            projectile = Projectile(self, self.game, direction)
            self.all_projectiles.add(projectile)
        if direction == 'down':
            projectile = Projectile(self, self.game, direction)
            self.all_projectiles.add(projectile)
        if direction == 'left':
            projectile = Projectile(self, self.game, direction)
            self.all_projectiles.add(projectile)
        if direction == 'right':
            projectile = Projectile(self, self.game, direction)
            self.all_projectiles.add(projectile)


    def reset_position(self):
        self.rect.x = 0
        self.rect.y = 0

    def move_right(self, amount=0):
        self.rect.x += self.velocity

    def move_left(self, amount=0):
        self.rect.x -= self.velocity

    def move_up(self, amount=0):
        self.rect.y -= self.velocity

    def move_down(self, amount=0):
        self.rect.y += self.velocity

    def update_health_bar(self,surface):
        pygame.draw.rect(surface,(60,60,60),[self.rect.x-8, self.rect.y-5, self.health_max,5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x-8,self.rect.y-5,self.health,5])

    def damage(self,amount):

        if self.health-amount>0:
            self.health -= amount
        else:
            self.game.game_over()

