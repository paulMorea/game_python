import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent

# seconde classe qui va representer notre jeu
class Game():

    def __init__(self):
        # definir si notre jeu a commencé ou non 
        self.is_playing = False

        # charger notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstres 
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 de vie, jeu en attente 
        self.all_monsters = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False

    def update(self , screen):
        # appliquer l'image de notre joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # recupere les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupere les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recupere les cometes 
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur souhaite aller a gauche ou a droite 
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)