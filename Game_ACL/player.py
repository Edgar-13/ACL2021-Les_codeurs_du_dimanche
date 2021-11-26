import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.ratio = 17
        self.image = pygame.image.load("assets/pacman.png")
        self.image = pygame.transform.scale(self.image, (self.game.screen_width / self.ratio,
                                                         self.game.screen_width / self.ratio))
        self.rect = self.image.get_rect()
        self.velocity = 2

    def reset_position(self):
        self.rect.x = 0
        self.rect.y = 0

    def move_right(self, amount=0):
        self.rect.x += self.velocity

    def move_left(self, amount=0):
        self.rect.x -= self.velocity

    def move_up(self, amount=0):
        self.rect.y -= self.velocity

    def move_down(self, amount=0):
        self.rect.y += self.velocity




