import pygame
import game
import monster


class Projectile_monster(pygame.sprite.Sprite):

    def __init__(self,game,direction,name,monster):
        super().__init__()
        self.game = game
        self.monster=monster
        self.direction = direction
        self.velocity = 2.5
        self.ratio = 15
        self.width = self.game.screen_width / self.ratio
        self.height = self.game.screen_height / self.ratio
        self.image = pygame.image.load(f'assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()
        self.direction = direction
        self.name = name
        self.rect.x = self.monster.rect.x
        self.rect.y = self.monster.rect.y

    # marche pas
    def remove(self):
        self.monster.all_projectiles_monster.remove(self)

    def move_up(self):
        self.rect.y -= self.velocity
        if self.rect.y <0 :
            self.remove()
        self.collision()

    def move_down(self):
        self.rect.y += self.velocity
        if self.rect.y > self.game.screen_height :
            self.remove()
        self.collision()

    def move_left(self):
        self.rect.x -= self.velocity
        if self.rect.x < 0 :
            self.remove()
        self.collision()

    def move_right(self):
        self.rect.x += self.velocity
        if self.rect.x > self.game.screen_width :
            self.remove()
        self.collision()

    def degats(self):
        self.game.player.damage(self.monster.attack_distance)

    def collision(self):
        if self.game.check_collision(self, self.game.all_obstacles):
            self.remove()
        if self.game.check_collision(self,self.game.all_player):
            self.degats()
            self.remove()