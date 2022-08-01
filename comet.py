import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 1000)
        self.rect.y = - random.randint(0, 800)
        self.velocity = random.randint(1, 2)

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # verifier si le nombre de cometes est de 0
        if len(self.comet_event.all_comets) == 0:
            print('l evenement est fini')
            # remettre la barre à 0
            self.comet_event.reset_percent()
            # apparaitre les 2 premiers monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol 
        if self.rect.y >= 500:
            print('sol!!!')

            # retirer la comete 
            self.remove()

            # s'il n'ya plus de comete 
            if len(self.comet_event.all_comets) == 0:
                # remettre la jauge au depart 
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
        
        # verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print('collision')

            # retirer la comete 
            self.remove()

            self.comet_event.game.player.damage(10)
