import pygame


# dimension de l'écran
screenLength = 1200 # length = width
screenHeigth = 800

# frame per second du jeu
fps = 120

# couleur de l'écran
background_color = (135, 206, 250)  # Bleu ciel

# hauteur des tuyaux minimun
pipeHeigthMin = 80

# largeur des tuyaux : calcul à partir des proportions : 180
pipeLength = 100

# difficulté : espace entre les tuyau, correspondant à (flappy bird = 4x la taille de l'oiseau = 240) ou obtenu par calculs de proportion : 228
difficulty = 230

# vitesse du jeu
gamespeed = 275  #unit/s 
# par des calculs de proportion selon les gameplays de flappy bird en prenant un oiseau de 30 unit de rayon

# spawn point du joueur
player_spawnpoint = pygame.Vector2(screenLength / 4, screenHeigth / 2)

# spawnrate des tuyaux : distance entre chaque tuyaux // obtenu par l'écran faisant 1200, on veut 4 tuyaux sur l'écran // ou 380 obtenu par calculs de proportion selon les gameplays
pipeDistance = 380

# taille du cercle du joueur : 
player_radius = 30

# size of the population :
size = 100

# gravité et jumping speed
g = 0.25
j = -7

# jump rate
jump_rate = 0.2

# learning rate 
learning_rate1 = 0.85  # in player / think <=> a jumping rate out of 1

# titre de l'écran 
titre = "Fl-AI-ppy Bird"

# hauteur du sol 
ground_level = screenHeigth * ( 95 / 100)