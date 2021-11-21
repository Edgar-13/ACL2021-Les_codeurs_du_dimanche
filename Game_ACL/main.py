import pygame
import math
from game import Game

pygame.init()

#def horloge
clock = pygame.time.Clock()
FPS = 50000

# Récupère la taille de notre écran
screen_info = pygame.display.Info()
screen_width = 3 * screen_info.current_w / 4
screen_height = 3 * screen_info.current_h / 4

#affichage bla
pygame.display.set_caption("jeu comette")
screen = pygame.display.set_mode((screen_width, screen_height))



background1 = pygame.image.load('assets/map1.jpg')
background1 = pygame.transform.scale(background1, (screen_width, screen_height))

game = Game(screen_info)


running=True
#boucle condition d'allumage
while running :



    #bg
    screen.blit(background1,(0,0))

    #verifié si jeu en cours
    if game.is_playing :
        game.update(screen)




    # mettre a jour ecran
    pygame.display.flip()


    #si on ferme
    for event in pygame.event.get():
        game.start()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #si joueur lache touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True




        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False



    #fixer le nbr de fps
    clock.tick(FPS)