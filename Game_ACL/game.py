import pygame
from player import Player
from monster import Ghost_red
from monster import Monster


class Game():
    def __init__(self):
        #definir si le jeu est en cours
        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.pressed = {}
        self.score = 0
        self.all_monsters = pygame.sprite.Group()
        self.font = pygame.font.Font("assets/SyneMono-Regular.ttf", 35)
        self.spawn_monster(Ghost_red)


    def spawn_monster(self,name):
        self.all_monsters.add(name.__call__(self))

    def start (self):
        self.is_playing = True
        # afficher les monstres



    def update(self,screen):
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

        # voir si on appui sur une touche

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y >0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height <screen.get_height():
            self.player.move_down()

    def game_over(self):
        self.player.health = self.player.health_max
        self.is_playing = False
        self.score = 0




    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

