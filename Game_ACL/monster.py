import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game, name, size,xm,ym, offset=0):
        super().__init__()
        self.game = game
        self.ratio = 17
        self.width = self.game.screen_width / self.ratio
        self.height = self.game.screen_height / self.ratio
        self.health = 100
        self.health_max = 100
        self.attack = 0.1
        self.image = pygame.image.load(f'assets/'+name+'.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = xm
        self.rect.y = ym


    def set_speed(self,speed):
        self.default_speed = speed
        self.velocity = 1

    def update_health_bar(self,surface):
        pygame.draw.rect(surface,(60,60,60),[self.rect.x + 15, self.rect.y - 20, self.health_max, 5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+15,self.rect.y-20,self.health,5])

    def move_alea(self):

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

    def __init__(self,game,xm,ym):
        super().__init__(game,'ghost_red',(230,230),xm,ym)
        self.health = 50
        self.health_max = 50
        self.attack = 0.5
        self.set_speed(2)
        self.point=2
