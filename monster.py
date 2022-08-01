import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        # self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1080 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.uniform(0.000001, 0.00001)
        self.start_animation()
    
    def damage(self, amount):
        # infliger les degats 
        self.health -= amount
        
        # verifier si son nouveau nombre de points de vie est inferieur ou égal à 0
        if self.health <= 0 :
            # reapparaitre comme un nouveau monstre 
            self.rect.x = 1080 + random.randint(0,300)
            self.velocity = random.uniform(0.000001, 0.00001)
            self.health = self.max_health

            # si la barre d'evenement est charge à son maximum
            if self.game.comet_event.is_full_loaded():
                # retirer monstre du jeu 
                self.game.all_monsters.remove(self)

                # appel pour declencher la pluie de cometes 
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie 
        bar_color = (0, 255, 38)

        # definir une couleur pour l'arriere plan de notre jauge de vie 
        back_bar_color = (250, 157, 157)

        # definir la position de notre jauge de vie ainsi que sa largeur + epaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        # definir la position de l'arriere plan de notre jauge de vie ainsi que sa largeur + epaisseur
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner notre jauge de vie 
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
    
    def forward(self):
        # le deplacement se fait que si il n'ya pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            self.game.player.damage(self.attack)
