import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__()
        self.game = game
        self.width = 100
        self.height = 100
        self.health = 100
        self.health_max = 100
        self.attack = 0.1
        self.image = pygame.image.load(f'assets/'+name+'.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 100


    def set_speed(self,speed):
        self.default_speed = speed
        self.velocity = 1

    def update_health_bar(self,surface):
        pygame.draw.rect(surface,(60,60,60),[self.rect.x + 15, self.rect.y - 20, self.health_max, 5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+15,self.rect.y-20,self.health,5])

    def move_alea(self):
        signe = ["x","y"]
        rand = random.randint(0, 4)
        if not self.game.check_collision(self,self.game.all_player):

            if rand == 0 :
                self.rect.y -= self.velocity

            elif rand == 1 :
                self.rect.y += self.velocity

            elif rand == 2:
                self.rect.x += self.velocity

            elif rand == 3:
                self.rect.x -= self.velocity
        else :
            self.game.player.dammage(self.attack)

class Ghost_red(Monster):

    def __init__(self,game):
        super().__init__(game,'ghost_red',(230,230))
        self.health = 50
        self.health_max = 50
        self.attack = 0.1
        self.set_speed(2)
        self.point=2
