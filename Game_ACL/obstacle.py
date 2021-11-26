import pygame


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.ratio = 15
        self.image = pygame.image.load("assets/rocks.png")
        self.image = pygame.transform.scale(self.image, (self.game.screen_width / self.ratio,
                                                         self.game.screen_width / self.ratio))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

