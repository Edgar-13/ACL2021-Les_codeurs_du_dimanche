import pygame



class Player():

    def __init__(self,game):
        self.width = 100
        self.height = 100
        self.health = 100
        self.health_max = 100
        self.attack = 30
        self.velocity = 2
        self.image = pygame.image.load(f'assets/pacman.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.x=0
        self.rect.y=0
        self.game=game


    def move_right(self):
        self.rect.x+=self.velocity

    def move_left(self):
        self.rect.x-=self.velocity

    def move_up(self):
        self.rect.y-=self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def update_health_bar(self,surface):
        pygame.draw.rect(surface,(60,60,60),[self.rect.x+5, self.rect.y, self.health_max,5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+5,self.rect.y,self.health,5])

    def dammage(self,amount):

        if self.health-amount>amount:
            self.health-=amount
        else:
            self.game.game_over()

