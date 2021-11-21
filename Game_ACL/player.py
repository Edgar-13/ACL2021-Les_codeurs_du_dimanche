import pygame



class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.width = 100
        self.height = 100
        self.health = 100
        self.health_max = 100
        self.attack = 30
        self.velocity = 5
        self.image = pygame.image.load(f'assets/pacman.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x=50
        self.rect.y=50
        self.game=game

        #stock le dernier mouvment
        self.last_move = "nothing"
        #sotck le dernier mouvement pour quand il y a collision
        self.last_move2= "nothing"
    def directions_possible(self,dir):

        if (len(self.game.check_collision(self, self.game.all_obstacles)) == 2 or len(self.game.check_collision(self, self.game.all_monsters))==2) and self.last_move2 ==str(dir):
            return False
        else:
            return (not self.game.check_collision(self, self.game.all_obstacles) and not self.game.check_collision(self,self.game.all_monsters)) or self.last_move != str(dir)

    def move_right(self):
        if self.directions_possible("right"):
            self.rect.x += self.velocity
            if (not self.game.check_collision(self, self.game.all_obstacles) and not self.game.check_collision(self, self.game.all_monsters)):
                self.last_move = "right"
            if self.game.check_collision(self, self.game.all_obstacles) or self.game.check_collision(self, self.game.all_monsters):
                self.last_move2 = "right"

    def move_left(self):
        if self.directions_possible("left"):
            self.rect.x -= self.velocity
            if (not self.game.check_collision(self, self.game.all_obstacles) and not self.game.check_collision(self, self.game.all_monsters)):
                self.last_move = "left"
            if self.game.check_collision(self, self.game.all_obstacles) or self.game.check_collision(self, self.game.all_monsters):
                self.last_move2 = "left"
    def move_up(self):
        if self.directions_possible("up"):
            self.rect.y-=self.velocity

            if (not self.game.check_collision(self, self.game.all_obstacles) and not self.game.check_collision(self, self.game.all_monsters)):
                self.last_move = "up"
            if self.game.check_collision(self, self.game.all_obstacles) or self.game.check_collision(self, self.game.all_monsters):
                self.last_move2 = "up"
    def move_down(self):
        if self.directions_possible("down"):
            self.rect.y += self.velocity
            if (not self.game.check_collision(self, self.game.all_obstacles) and not self.game.check_collision(self, self.game.all_monsters)):
                self.last_move = "down"
            if self.game.check_collision(self, self.game.all_obstacles) or self.game.check_collision(self, self.game.all_monsters):
                self.last_move2 = "down"

    def update_health_bar(self,surface):
        pygame.draw.rect(surface,(60,60,60),[self.rect.x+5, self.rect.y, self.health_max,5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+5,self.rect.y,self.health,5])

    def dammage(self,amount):

        if self.health-amount>amount:
            self.health-=amount
        else:
            self.game.game_over()

