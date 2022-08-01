import pygame
from projectile import Projectile

# classe qui va representer notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 2
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 440
        self.rect.y = 500
    
    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
        # si le joueur n'a plus de point de vie
            self.game.game_over()
        

    def update_health_bar(self, surface):
        # dessiner notre jauge de vie 
        pygame.draw.rect(surface, (250, 157, 157), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (0, 255, 38), [self.rect.x + 50, self.rect.y + 20, self.health, 7])
    
    def launch_projectile(self):
        # creer une nouvelle instance de projectile 
        # projectile = Projectile()
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if  not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity