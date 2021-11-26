import pygame
from game import Game

pygame.init()

# Récupère la taille de notre écran
screen_info = pygame.display.Info()
relation = 5 / 6
screen_width = relation * screen_info.current_w
screen_height = relation * screen_info.current_h

game = Game(screen_width, screen_height)

# Générer la fenêtre du jeu
pygame.display.set_caption("Pacman")
screen = pygame.display.set_mode((screen_width, screen_height))

# Arrière plan 0
background_0 = pygame.image.load("assets/background_0.bmp")
background_0 = pygame.transform.scale(background_0, (screen_width, screen_height))

# Arrière plan 1
background_1 = pygame.image.load("assets/background_1.bmp")
background_1 = pygame.transform.scale(background_1, (screen_width, screen_height))

# Arrière plan 2
background_2 = pygame.image.load("assets/background_2.bmp")
background_2 = pygame.transform.scale(background_2, (screen_width, screen_height))

# End
end = pygame.image.load("assets/end.bmp")
end = pygame.transform.scale(end, (screen_width / 17, 2 * screen_height / 17))
end_rect = end.get_rect()
end_rect.center = (screen_width - screen_width / 34, screen_height - 2 * screen_height / 34)

# Bouton Jouer
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (screen_width / 3, screen_height / 3))
play_button_rect = play_button.get_rect()
play_button_rect.center = (screen_width / 2, screen_height / 2)


running = True

while running:

    if game.is_playing1:
        screen.blit(background_1, (0, 0))
        screen.blit(end, end_rect)
        game.update(screen)
        if game.player.rect.colliderect(end_rect):
            game.start2()
    elif game.is_playing2:
        screen.blit(background_2, (0, 0))
        screen.blit(end, end_rect)
        game.update(screen)
    else:
        screen.blit(background_0, (0, 0))
        screen.blit(play_button, play_button_rect)

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
                game.start1()

