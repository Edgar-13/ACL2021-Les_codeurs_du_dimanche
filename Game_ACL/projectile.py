import pygame
import game
from obstacles import Obstacles


# définir la classe qui va gérer le  projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #définir le constructeur de cette classe
    def __init__(self,player,game,direction):
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
        self.rect.y = player.rect.y + player.height/2 - self.height/2
        self.direction = direction


    def remove(self):
        self.player.all_projectiles.remove(self)


    #Pour les questre directions, on vérifie que le projectile n'est plus present sur l'ecran, puis on le supprime
    def move_up(self):
        self.rect.y -= self.velocity
        if self.rect.y <0 :
            self.remove()
        elif self.player.game.check_collision(self, self.player.game.all_obstacles) or self.player.game.check_collision(self,self.player.game.all_monsters):
            self.remove()
            #dégat monstre
 #       for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
 #           #infliger dégâts au monstre
 #           monster.damage(self.player.attack)
 #           self.remove()
    def move_down(self):
        self.rect.y += self.velocity
        if self.rect.y > self.game.screen_height :
            self.remove()
        elif self.player.game.check_collision(self, self.player.game.all_obstacles) or self.player.game.check_collision(self,self.player.game.all_monsters):
            self.remove()

    def move_left(self):
        self.rect.x -= self.velocity
        if self.rect.x < 0 :
            self.remove()
        elif self.player.game.check_collision(self, self.player.game.all_obstacles) or self.player.game.check_collision(self,self.player.game.all_monsters):
            self.remove()
    def move_right(self):
        self.rect.x += self.velocity
        if self.rect.x > self.game.screen_width :
            self.remove()
        elif self.player.game.check_collision(self, self.player.game.all_obstacles) or self.player.game.check_collision(self,self.player.game.all_monsters):
            self.remove()
