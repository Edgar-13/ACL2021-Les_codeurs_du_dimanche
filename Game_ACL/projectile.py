import pygame
import game

# définir la classe qui va gérer le  projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #définir le constructeur de cette classe
    def __init__(self,player,game):
        super().__init__()
        self.velocity = 8
        self.ratio = 15
        self.game = game
        self.player = player
        self.width = self.game.screen_width / self.ratio
        self.height = self.game.screen_height / self.ratio
        self.image = pygame.image.load(f'assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.width/2 - self.width/2
        self.rect.y = player.rect.y + player.height/2 - self.width/2


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        #verifier si notre projectile n'est plus present sur l'ecran
        if self.rect.x > self.game.screen_width :
            #on le supprime
            self.remove()




