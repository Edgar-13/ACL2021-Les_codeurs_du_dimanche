import pygame
from player import Player



class Game():
    def __init__(self):
        #definir si le jeu est en cours
        self.is_playing = False
        self.player = Player(self)
        self.pressed = {}
        self.score = 0
        self.font = pygame.font.Font("assets/SyneMono-Regular.ttf", 35)



    def start (self):
        self.is_playing = True

    def update(self,screen):
        #afficher score

        score_text = self.font.render(f"Score : {self.score}",1,(0,0,0))
        screen.blit(score_text,(20,20))

        # joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

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
        self.sound_manager.play('game_over')
        pygame.mixer.music.stop()




    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

