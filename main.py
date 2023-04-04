import pygame
from game import Game
from player import Player
pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Pygame Azmog")
screen = pygame.display.set_mode((1080, 720))

# importer de charger l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# charger le jeu
game = Game()

# charger notre joueur
player = Player()

running =  True 

# boucle tant que cette condition est vrai 
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # verifier si le joueur veut aller à gauche ou a droite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        game.player.move_right()
    elif keys[pygame.K_LEFT]:
        game.player.move_left()

    # mettre à jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre 
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #detecter si un joueur lache une touche du clavier 
        elif event.type == pygame.KEYDOWN:
            pygame.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            pygame.pressed[event.key] = False