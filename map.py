import pygame
import settings
import random


class Ground:
    thickness = settings.screenHeigth / 10
    color = (0, 204, 0)

    def __init__(self):
        self.x, self.y = 0, settings.ground_level
        self.ground = pygame.Rect(self.x, self.y, settings.screenLength, Ground.thickness)

    def draw(self, window):
        pygame.draw.rect(window, Ground.color, self.ground)

class Pipes:
    length = settings.pipeLength # largeur des tuyaux : calcul à partir des proportions : 180
    opening = settings.difficulty # cf settings
    deltaPipe = 10  # longueur de sécurité pour la taille des tuyaux graphiquement
    color = "green"

    def __init__(self):
        self.x = settings.screenLength
        self.top_height = random.randint(settings.pipeHeigthMin, settings.screenHeigth - settings.difficulty - settings.pipeHeigthMin) + Pipes.deltaPipe
        self.bottom_height = settings.screenHeigth - self.top_height - settings.difficulty + Pipes.deltaPipe 
        self.bottom_rect, self.top_rect = pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)
        self.passed = False
        self.counted = False
        self.off_screen = False

    def draw(self, window):
        self.bottom_rect = pygame.Rect(self.x, settings.screenHeigth - self.bottom_height, self.length, self.bottom_height)
        pygame.draw.rect(window, Pipes.color, self.bottom_rect)

        self.top_rect = pygame.Rect(self.x, 0, self.length, self.top_height)
        pygame.draw.rect(window, Pipes.color, self.top_rect)

    def update(self, dt):
        # calcul des nouvelles coordonnées x de Down et Up
        self.x = self.x - settings.gamespeed * dt
        if self.x + Pipes.length <= settings.player_spawnpoint.x:
            self.passed = True
        if self.x <= -Pipes.length:
            self.off_screen = True


# sol du jeu 
sol = Ground()

# stockage des tuyaux 
pipes = [Pipes()]

















    #     ### un pipe étant donnée par (x,y,l,h) où x et y sont les coordonnées de son coin supérieur gauche, h et l sont sa hauteur et sa longueur (=pipeLength)
    # ### pipeMap est du type [(down,up)] où down = up = (x,y,l,h)

    # def pipeSpawn():  # renvoye un couple de pipe initialisé = (down,up) (situé juste en dehors de l'écran (à sa droite))
    #     deltaPipe = 10 # longueur de sécurité pour la taille des tuyaux graphiquement
    #     hauteurUp = random.randint(settings.pipeHeigthMin, settings.screenHeigth - settings.difficulty - settings.pipeHeigthMin) + deltaPipe
    #     hauteurDown = settings.screenHeigth - hauteurUp - settings.difficulty + deltaPipe
    #     up = (1200 + deltaPipe, -deltaPipe, settings.pipeLength, hauteurUp,False)
    #     down = (1200 + deltaPipe, hauteurUp + settings.difficulty, settings.pipeLength, hauteurDown)
    #     return ([(down, up)])
        

    # def obstacle(pipeMap,dt):
    #     # spawn et update la position des tuyaux // renvoye une file d'attente pipeMap contenant des couples de tuyau (downPipe, upPipe) à dessiner sur la map
    #     # les nouveaux tuyaux qui spawn sont ajouter en fin de liste (à sa droite) car ils apparaitront à la droite de l'écran
    #     # dès qu'un tuyau sort de l'écran (par la gauche) ce dernier est en position 0 (pipeMap[0]) il suffira de le pop

    #     # update la position des pipes déjà existant
    #     for i in range(len(pipeMap)):
    #         down, up = pipeMap[i]
    #         pipeMap[i] = updatedPipes(down,up,dt)
    #     # création de nouveau pipe si nécessaire
    #     downLast, upLast = pipeMap[len(pipeMap) - 1]
    #     (xLast, yLast, lLast, hLast) = downLast
    #     xNewElement = settings.screenLength - settings.pipeDistance
    #     if xLast < xNewElement : 
    #         pipeMap = pipeMap + pipeSpawn()
    #     # suppression du premier pipe (pipeMap[0], celui le plus à droite hors de l'écran) si nécessaire
    #     downFirst, upFirst = pipeMap[0]
    #     (xFirst, yFirst, lFirst,  hFirst) = downFirst
    #     if xFirst < -5-settings.pipeLength : # par sécurité on ne met pas 0
    #         pipeMap.pop(0)
    #     return (pipeMap)
        
