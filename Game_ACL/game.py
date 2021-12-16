import random

import pygame

import player
from player import Player
from monster import Ghost_red,Ghost_blue
from obstacles import Obstacles
from projectileMonster import Projectile_monster
from projectile import Projectile
import monster

class Game():
    def __init__(self, screen_width, screen_height):
       #taille écran
        self.screen_width = screen_height
        self.screen_height = screen_height
        #niveau actif
        self.niveau = 0
        # nombre de niveau - 1
        self.nbr_niveau = 2
        #definir si le jeu est en cours
        self.is_playing = False

        #groupe de sprite joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.pressed = {}
        self.score = 0

        "monstres"
        self.all_monsters = pygame.sprite.Group()
        #liste des monstres par niveau
        self.m = [[[Ghost_red,400,300],[Ghost_blue,350,400]],
                    [[Ghost_red, 100,500],[Ghost_blue,500,50]],
                    [[Ghost_blue,100,300],[Ghost_red,500,500]]]


        "obstacles"
        self.all_obstacles = pygame.sprite.Group()
        #list des obstacles par niveau (1 nv par ligne)
        self.ob = [[[self.screen_height / 20, self.screen_width/5, 200, 500],[self.screen_height / 20, self.screen_width/5, 500, 100]],
                    [[self.screen_height / 20, self.screen_width/5, 500, 500],[self.screen_height / 20, self.screen_width/5, 100, 100]],
                    [[self.screen_height / 20, self.screen_width/5, 500, 500],[self.screen_height / 20, self.screen_width/5, 100, 100]]]


        #création spite arrivée
        self.end = pygame.image.load("assets/end.bmp")
        self.end = pygame.transform.scale(self.end, (self.screen_width / 10, self.screen_width / 10))
        self.end_rect = self.end.get_rect()
        self.end_rect.center = (self.screen_width - self.screen_width / 20, self.screen_height - 2 * self.screen_height / 40)

        #choix police pour score
        self.font = pygame.font.Font("assets/SyneMono-Regular.ttf", 35)

        #timer
        self.start_timer = 3000000
        self.secondes = self.start_timer

        self.reset=True
        self.var=300
        self.condition=True


    def ajouter_obstacle(self,largeur,hauteur,x,y):
        obstacles = Obstacles(largeur,hauteur,x,y)
        self.all_obstacles.add(obstacles)

    def spawn_monster(self,name,xm,ym):
        self.all_monsters.add(name.__call__(self,xm,ym))
        # self.monster=Ghost_red(self)
        # self.all_monsters.add(monster)

    def start (self):
        self.is_playing = True
        # afficher les monstres



    def update(self,screen):
        #on vides les groupes de sprites puis on les affiches : pb car on les creers en boucles et supr en boucle
        if self.reset:
            self.all_obstacles.empty()
            self.all_monsters.empty()
            for obst in self.ob[self.niveau]:
                self.ajouter_obstacle(obst[0],obst[1],obst[2],obst[3])
            for mst in self.m[self.niveau]:
                self.spawn_monster(mst[0],mst[1],mst[2])
            self.reset=False

        # gerer temps
        self.secondes =(self.secondes - 50)
        secondes = int(self.secondes/1000)
        if self.secondes < 0.0:
            self.game_over()
        time_text = self.font.render(f"Temps : {secondes}", True, (0, 0, 0))
        screen.blit(time_text, (220, 20))

        # afficher score
        score_text = self.font.render(f"Score : {self.score}",True,(0,0,0))
        screen.blit(score_text,(20,20))

        # joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        # recuperer les projectiles de joueur
        for projectile in self.player.all_projectiles:
            if projectile.direction == 'up':
                projectile.move_up()
            if projectile.direction == 'down':
                projectile.move_down()
            if projectile.direction == 'right':
                projectile.move_right()
            if projectile.direction == 'left':
                projectile.move_left()

        #appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # afficher les monstres
        self.all_monsters.draw(screen)

        # end
        screen.blit(self.end, self.end_rect)

        #monstres
        #Je test des déplacements
        change=True
        for monster in self.all_monsters:
            monster.update_health_bar(screen)
            monster.all_projectiles_monster.draw(screen)
            # if change:
            #     if self.condition:
            #         monster.move_right()
            #         if monster.rect.x>=self.var+300:
            #             # self.var=-self.var
            #             self.condition = False
            #     else:
            #         monster.move_left()
            #         if monster.rect.x<= 400-self.var:
            #             self.condition=True
                # change=False
            # if not change :
            #     if self.condition:
            #         monster.move_down()
            #         if monster.rect.y>=self.var+300:
            #             # self.var=-self.var
            #             self.condition = False
            #     else:
            #         monster.move_up()
            #         if monster.rect.x<= 400-self.var:
            #             self.condition=True
            #     change=True
            if not self.player.rect.colliderect(monster):
                #monster.move_alea()
                monster.move_easy(monster.name)
                r=random.randint(1,400)
                if r<=2:
                    monster.shot(monster.name)
                for projectile in monster.all_projectiles_monster:
                     if projectile.direction=='down':
                        projectile.move_left()
                     if projectile.direction=='up':
                        projectile.move_right()
                     if projectile.direction=='right':
                        projectile.move_left()
                     if projectile.direction=='left':
                        projectile.move_right()

            else:
                self.player.damage(monster.attack)

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # afficher les obstacles
        self.all_obstacles.draw(screen)

        # voir si on reste appuier sur une touche

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < self.screen_width:
            self.player.move_right()
            if self.check_collision(self.player, self.all_obstacles) or self.check_collision(self.player, self.all_monsters):
                self.player.move_left()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -5:
            self.player.move_left()
            if self.check_collision(self.player, self.all_obstacles) or self.check_collision(self.player, self.all_monsters):
                self.player.move_right()

        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
            if self.check_collision(self.player, self.all_obstacles) or self.check_collision(self.player, self.all_monsters):
                self.player.move_down()

        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < self.screen_height - 5:
            self.player.move_down()
            if self.check_collision(self.player, self.all_obstacles) or self.check_collision(self.player, self.all_monsters):
                self.player.move_up()

        if self.player.rect.colliderect(self.end_rect) and self.niveau<=1 :
            self.player.reset_position()
            self.niveau += 1
            self.score+=100
            self.reset = True
        elif self.player.rect.colliderect(self.end_rect) and self.niveau==self.nbr_niveau:
            self.game_over()



    def game_over(self):
        self.is_playing = False
        self.player.health = self.player.health_max
        self.player.reset_position()
        self.niveau = 0
        self.score = 0
        self.secondes = self.start_timer
        self.reset=True

    def end(self): # a mieux def
        self.player.health = self.player.health_max
        self.player.reset_position()
        self.niveau = 0
        self.is_playing = False
        self.score = 0
        self.reset=True


    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
