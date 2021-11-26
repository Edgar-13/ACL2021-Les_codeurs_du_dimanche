import pygame
import game


class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.ratio = 10
        self.width = self.game.screen_width/self.ratio
        self.height = self.game.screen_height/self.ratio
        self.health = 80
        self.health_max = 80
        self.attack = 30
        self.velocity = 5
        self.image = pygame.image.load(f'assets/pacman.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x=50
        self.rect.y=50
        self.game=game

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
        pygame.draw.rect(surface,(60,60,60),[self.rect.x+5, self.rect.y, self.health_max,5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+5,self.rect.y,self.health,5])

    def dammage(self,amount):

        if self.health-amount>amount:
            self.health-=amount
        else:
            self.game.game_over()

