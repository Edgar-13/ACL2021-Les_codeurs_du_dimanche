import pygame
from player import Player
from monster import Ghost_red
from monster import Monster
from obstacles import Obstacles

class Game():
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_height
        self.screen_height = screen_height
        #niveau actif
        self.niveau = 0
        self.end_rect = [self.screen_width - self.screen_width / 20, self.screen_height - 2 * self.screen_height / 38]


        #definir si le jeu est en cours
        self.is_playing = False
        #groupe de sprite joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.pressed = {}

        self.score = 0

        #monstres
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster(Ghost_red,100,500)
        #obstacles
        self.all_obstacles =pygame.sprite.Group()
        self.font = pygame.font.Font("assets/SyneMono-Regular.ttf", 35)
        #ajout des murs autour
        # mur de gauche
        # self.ajouter_obstacle(self.screen_width, self.screen_height / 50, 0, 0)
        # # mur de droite
        # self.ajouter_obstacle(self.screen_width, self.screen_height / 50, self.screen_width - self.screen_height / 52, 0)
        # # mur du haut
        # self.ajouter_obstacle(self.screen_height / 50, self.screen_width, 0, 0)
        # # mur du bas
        # self.ajouter_obstacle(self.screen_height / 50, self.screen_width, 0, self.screen_height - self.screen_height / 52)

        #list des obstacles par niveau
        self.ob = [[[self.screen_height / 20, self.screen_width/5, 200, 500],[self.screen_height / 20, self.screen_width/5, 500, 100]],[[self.screen_height / 20, self.screen_width/5, 500, 500],[self.screen_height / 20, self.screen_width/5, 100, 100]],[]]


    def ajouter_obstacle(self,largeur,hauteur,x,y):
        obstacles = Obstacles(largeur,hauteur,x,y)
        self.all_obstacles.add(obstacles)

    def spawn_monster(self,name,xm,ym):
        self.all_monsters.add(name.__call__(self,xm,ym))

    def start (self):
        self.is_playing = True
        # afficher les monstres



    def update(self,screen):
        self.all_obstacles.empty()
        for obst in self.ob[self.niveau]:
            self.ajouter_obstacle(obst[0],obst[1],obst[2],obst[3])


        #afficher score

        score_text = self.font.render(f"Score : {self.score}",1,(0,0,0))
        screen.blit(score_text,(20,20))

        # joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        #monstres
        for monster in self.all_monsters:
            monster.update_health_bar(screen)
            monster.move_alea()

        # afficher les monstres
        self.all_monsters.draw(screen)

        # afficher les monstres
        self.all_obstacles.draw(screen)

        # voir si on appui sur une touche

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

        if self.check_collision(self.player, self.all_monsters) and self.niveau<=1 :
            self.player.reset_position()
            self.niveau += 1



    def game_over(self):
        self.player.health = self.player.health_max
        self.is_playing = False
        self.score = 0




    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

