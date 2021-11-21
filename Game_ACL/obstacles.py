import pygame

class Obstacles(pygame.sprite.Sprite):

    def __init__(self, hauteur, largeur, x, y):
        super().__init__()
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = x
        self.y = y
        self.image = pygame.image.load(f'assets/murs.png')
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

