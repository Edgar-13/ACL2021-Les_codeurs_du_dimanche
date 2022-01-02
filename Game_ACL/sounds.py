import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'ambiance': pygame.mixer.Sound("assets/sounds/ghost_fight_undertale.mp3"),
            'game_over' : pygame.mixer.Sound("assets/sounds/game_over.mp3"),
            'shoot' : pygame.mixer.Sound("assets/sounds/shoot.mp3"),
            'bonus' : pygame.mixer.Sound("assets/sounds/bonus.mp3")
        }

    def play(self,name):
        # if name=='shoot':
        self.sounds[name].play()
        # else:
        #     self.sounds[name].play()
