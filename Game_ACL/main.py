import pygame

from game import Game

pygame.init()

#def horloge 2
clock = pygame.time.Clock()
FPS = 50000

# Récupère la taille de notre écran 2
screen_info = pygame.display.Info()
relation = 3 / 4
screen_width = relation*screen_info.current_h
screen_height = relation*screen_info.current_h

#affichage

screen = pygame.display.set_mode((screen_width, screen_height))

background1 = pygame.image.load('assets/background_1.bmp')
background1 = pygame.transform.scale(background1, (screen_width, screen_height))


game = Game(screen_width, screen_height)

# End
end = pygame.image.load("assets/end.bmp")
end = pygame.transform.scale(end, (screen_width / 10, screen_width / 10))
end_rect = end.get_rect()
end_rect.center = (screen_width - screen_width / 20, screen_height - 2 * screen_height / 40)

# Bouton Jouer
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (screen_width / 3, screen_height / 3))
play_button_rect = play_button.get_rect()
play_button_rect.center = (screen_width/2 , screen_height /2)

running = True
#boucle condition d'allumage
while running:





    #verifié si jeu en cours et choisir le bg
    if game.is_playing:
        background = pygame.image.load('assets/background_' + str(game.niveau) + '.bmp')
        background = pygame.transform.scale(background, (screen_width, screen_height))
        screen.blit(background, (0, 0))
        # end
        screen.blit(end, end_rect)
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)


    # mettre a jour ecran
    pygame.display.flip()

    # Si le joueur ferme cette fenêtre
    for event in pygame.event.get():

        # Si c'est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Si le joueur appuie sur une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        # Si le joueur lâche une touche
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # Pointeur de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Boutton jouer
            if play_button_rect.collidepoint(event.pos):
                # Lancer le jeu
                game.start()

    #fixer le nbr de fps
    clock.tick(FPS)