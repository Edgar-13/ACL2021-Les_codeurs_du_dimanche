import pygame
import random
import game


class Bonus(pygame.sprite.Sprite):

    def __init__(self, game, name, size,xm,ym, offset=0):
        super().__init__()
        self.game = game
        self.ratio = 17
        self.width = self.game.screen_width / self.ratio
        self.height = self.game.screen_height / self.ratio


    def remove(self):
        self.game.all_bonus.remove(self)


class CinquantePoints(Bonus):

    def __init__(self,game,xm,ym):
        super().__init__(game,'50points',(230,230),xm,ym)
        self.point = 50
        self.vitesse = 0
        self.vie = 0
        self.name=CinquantePoints
        self.image = pygame.image.load(f'assets/50points.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = xm
        self.rect.y = ym

class CentPoints(Bonus):

    def __init__(self,game,xm,ym):
        super().__init__(game,'100points',(230,230),xm,ym)
        self.point = 100
        self.vitesse = 0
        self.vie = 0
        self.name=CentPoints
        self.image = pygame.image.load(f'assets/100points.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = xm
        self.rect.y = ym

class LIFE(Bonus):

    def __init__(self,game,xm,ym):
        super().__init__(game,'LIFE',(230,230),xm,ym)
        self.point = 0
        self.vitesse = 0
        self.vie = 20
        self.name=LIFE
        self.image = pygame.image.load(f'assets/LIFE.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = xm
        self.rect.y = ym

class VEL(Bonus):

    def __init__(self,game,xm,ym):
        super().__init__(game,'VEL',(230,230),xm,ym)
        self.point = 0
        self.vitesse = 2
        self.vie = 0
        self.name=VEL
        self.image = pygame.image.load(f'assets/VEL.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = xm
        self.rect.y = ym

class StopShoot(Bonus):

    def __init(self,game,xm,ym):
        super().__init__(game,"StopShoot",(230,230),xm,ym)
        self.point = 0
        self.vitesse = 0
        self.vie = 0
        self.name = StopShoot
        self.image = pygame.image.load(f'assets/VEL.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = xm
        self.rect.y = ym

