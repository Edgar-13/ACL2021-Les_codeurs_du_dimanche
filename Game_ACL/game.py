import pygame
from player import Player
from monster import Ghost_red
from obstacles import Obstacles

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
        self.m = [[[Ghost_red,100,500],[Ghost_red,500,500]],
                    [[Ghost_red,100,500],[Ghost_red,500,50]],
                    [[Ghost_red,100,50],[Ghost_red,500,500]]]



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
        self.all_monsters.empty()
        for obst in self.ob[self.niveau]:
            self.ajouter_obstacle(obst[0],obst[1],obst[2],obst[3])

        for mst in self.m[self.niveau]:
            self.spawn_monster(mst[0],mst[1],mst[2])



        #afficher score

        score_text = self.font.render(f"Score : {self.score}",True,(0,0,0))
        screen.blit(score_text,(20,20))

        # joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        
        # end
        screen.blit(self.end, self.end_rect)

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

        if self.player.rect.colliderect(self.end_rect) and self.niveau<=1 :
            self.player.reset_position()
            self.niveau += 1
            self.score+=100



    def game_over(self):
        self.player.health = self.player.health_max
        self.player.reset_position()
        self.niveau = 0
        self.is_playing = False
        self.score = 0




    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

