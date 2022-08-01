import pygame
from game import Game
pygame.init()


# generer la fenetre de notre jeu
pygame.display.set_caption("Paul game")
screen = pygame.display.set_mode((1080, 720))

# importer charger l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# importer charger la banniere 
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = (screen.get_width() / 2) - (banner.get_width() / 2)
banner_rect.y = (screen.get_height() /2) - (banner.get_height() / 1.5)

# importer charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = (screen.get_width() / 2) - (play_button.get_width() / 2)
play_button_rect.y = (screen.get_height() / 2) + 25

# charger notre jeu
game = Game()

running =  True

# boucle tant que cette condition est vrai
while running:
    # appliquer l'arriere plan du jeu
    screen.blit(background, (0,-200))

    # verifier si notre jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie 
        game.update(screen)
    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon bouton
        screen.blit(play_button, play_button_rect)
        # ajouter mon ecran de bienvenue 
        screen.blit(banner, banner_rect)
        

    # mettre à jour l'ecran
    pygame.display.flip()


    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fentre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer notre projectile 
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False    
         
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.start() 
