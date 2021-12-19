import pygame
import random
import game
# from projectile import Projectiled
# from projectile import Projectile_monster
import projectile
from projectileMonster import Projectile_monster

class Monster(pygame.sprite.Sprite):

    def __init__(self, game, name, size,xm,ym, offset=0):
        super().__init__()
        self.game = game
        self.projectile = projectile
        self.ratio = 17
        self.width = self.game.screen_width / self.ratio
        self.height = self.game.screen_height / self.ratio
        self.health = 100
        self.health_max = 100
        # self.attack = 0.01
        # self.attack_distance = 20
        self.all_projectiles_monster = pygame.sprite.Group()
        # self.image = pygame.image.load(f'assets/'+name+'.png')
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # self.rect = self.image.get_rect()
        # self.rect.x = xm
        # self.rect.y = ym
        self.condition_red = True
        self.condition_blue = True
        self.var = 300

    def damage(self,amount):
        #infliger des dégats avec projectile
        self.health -= amount


    def set_speed(self,speed):
        self.default_speed = speed
        self.velocity = random.randint(3,self.default_speed)

    def update_health_bar(self,surface):
        pygame.draw.rect(surface,(60,60,60),[self.rect.x + 15, self.rect.y - 20, self.health_max, 5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+15,self.rect.y-20,self.health,5])

    def remove(self):
        self.game.all_monsters.remove(self)

    def move_alea(self):
        if not self.game.check_collision(self, self.game.all_player):
            rand=random.randint(0,4)

            if rand == 0:
                self.rect.y -= self.velocity

            elif rand == 1:
                self.rect.y += self.velocity

            elif rand == 2:
                self.rect.x += self.velocity

            elif rand == 3:
                self.rect.x -= self.velocity
        else:
                # infliger des dégâts
                self.game.player.damage(self.attack)

    def move_easy(self,name):
        #haut en bas si bleu, gauche à droite si rouge
        if self.game.check_collision(self,self.game.all_obstacles):
            if self.condition_red:
                self.condition_red=False
            else:
                self.condition_red=True
        if self.rect.x>200*self.game.screen_width/810:
            limit_right = 750*self.game.screen_width/810
            limit_left = 250*self.game.screen_width/810
        else:
            limit_right = 200*self.game.screen_width/810
            limit_left = 0
        if name == Ghost_red:
            if self.condition_red:
                self.move_right()
                if self.rect.x>=limit_right:
                    self.condition_red = False
            else:
                self.move_left()
                if self.rect.x<= limit_left:
                    self.condition_red=True
        if self.game.check_collision(self,self.game.all_obstacles):
            if self.condition_blue:
                self.condition_blue=False
            else:
                self.condition_blue=True
        if name == Ghost_blue:
            if self.condition_blue:
                self.move_right()
                if self.rect.x>=self.var+300*self.game.screen_width/810:
                    self.condition_blue = False
            else:
                self.move_left()
                if self.rect.x<= 10*self.game.screen_width/810:
                    self.condition_blue=True


    def move_left(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else :
            #infliger des dégâts
            self.game.player.damage(self.attack)

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x += self.velocity
        else :
            #infliger des dégâts
            self.game.player.damage(self.attack)

    def move_up(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.y -= self.velocity
        else :
            #infliger des dégâts
            self.game.player.damage(self.attack)

    def move_down(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.y += self.velocity
        else :
            #infliger des dégâts
            self.game.player.damage(self.attack)

    def shot_4Directions(self,name):
        if name==Ghost_blue:
            n=self.game.secondes
            n0 = self.game.start_timer
            test=(n0 - n) % 6000
            if test == 1450:
                #self.projectile.move_right()
        # creer une nouvelle instance de la classe Projectile_monster
                projectile = Projectile_monster(self.game, 'up', name,self)
                self.all_projectiles_monster.add(projectile)
            if test == 2900:
                projectile = Projectile_monster(self.game, 'left', name,self)
                self.all_projectiles_monster.add(projectile)
            if test == 4350:
                projectile = Projectile_monster(self.game, 'right', name,self)
                self.all_projectiles_monster.add(projectile)
            if test == 5800:
                projectile = Projectile_monster(self.game, 'down', name,self)
                self.all_projectiles_monster.add(projectile)



class Ghost_red(Monster):

    def __init__(self,game,xm,ym):
        super().__init__(game,'Ghost_red',(230,230),xm,ym)
        self.health = 50
        self.health_max = 50
        self.attack = 0.5
        self.set_speed(7)
        self.point=2
        self.name=Ghost_red
        self.image = pygame.image.load(f'assets/Ghost_red.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = xm
        self.rect.y = ym

class Ghost_blue(Monster):

    def __init__(self,game,xm,ym):
        super().__init__(game,'Ghost_blue',(230,230),xm,ym)
        self.health=50
        self.health_max=50
        self.attack=0.3
        self.attack_distance=20
        self.set_speed(4)
        self.point=2
        self.name=Ghost_blue
        self.image = pygame.image.load(f'assets/Ghost_blue.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = xm
        self.rect.y = ym



