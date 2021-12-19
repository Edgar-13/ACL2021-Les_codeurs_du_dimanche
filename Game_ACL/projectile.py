import pygame
import game
from obstacles import Obstacles
import monster

# définir la classe qui va gérer le  projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #définir le constructeur de cette classe
    def __init__(self,player,game,direction):
        super().__init__()
        self.velocity = 10
        self.ratio = 15
        self.game = game
        self.player = player
        self.width = self.game.screen_width / self.ratio
        self.height = self.game.screen_height / self.ratio
        self.image = pygame.image.load(f'assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()
        self.direction = direction
        self.monster = monster
        self.rect.x = player.rect.x + player.width/2 - self.width/2
        self.rect.y = player.rect.y + player.height/2 - self.height/2

    def remove(self):
        self.player.all_projectiles.remove(self)

    def collision(self):
        if self.player.game.check_collision(self, self.player.game.all_obstacles) or self.player.game.check_collision(self,self.player.game.all_monsters):
            self.remove()


    #Pour les quatre directions, on vérifie que le projectile n'est plus present sur l'ecran, puis on le supprime
    def move_up(self):
        self.rect.y -= self.velocity
        if self.rect.y <0 :
            self.remove()
        self.collision()
        # dégâts monstre
        self.degats()

    def move_down(self):
        self.rect.y += self.velocity
        if self.rect.y > self.game.screen_height :
            self.remove()
        self.collision()
        # dégâts monstre
        self.degats()

    def move_left(self):
        self.rect.x -= self.velocity
        if self.rect.x < 0 :
            self.remove()
        self.collision()
        # dégâts au monstre
        self.degats()

    def move_right(self):
        self.rect.x += self.velocity
        if self.rect.x > self.game.screen_width :
            self.remove()
        self.collision()
        # dégâts au monstre
        self.degats()

    def degats(self):
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            monster.damage(self.player.attack)
            if monster.health <= 0:
                monster.remove()



# class Projectile_monster(pygame.sprite.Sprite):
#
#     def __init__(self,game,direction,name):
#         super().__init__()
#         self.game = game
#         self.direction = direction
#         self.velocity = 2
#         self.ratio = 15
#         self.width = self.game.screen_width / self.ratio
#         self.height = self.game.screen_height / self.ratio
#         self.image = pygame.image.load(f'assets/projectile.png')
#         self.image = pygame.transform.scale(self.image, (self.width,self.height))
#         self.rect = self.image.get_rect()
#         self.direction = direction
#         self.name = name
#         self.rect.x = self.rect.x + self.width/2 - self.width/2
#         self.rect.y = self.rect.y + self.height/2 - self.height/2
#         self.all_projectiles_monster = pygame.sprite.Group()

    # # marche pas
    # def remove(self):
    #     self.all_projectiles_monster.remove(self)
    #
    # def move_down(self):
    #     self.rect.y += self.velocity
    #
    # def move_up(self):
    #     self.rect.y -= self.velocity
    #
    # def move_right(self):
    #     self.rect.x += self.velocity
    #
    # def move_left(self):
    #     self.rect.x -= self.velocity


