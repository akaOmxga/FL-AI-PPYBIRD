import pygame
import settings
import math
import random

def distance(pointA, pointB):  # renvoye la distance entre le point A et le point B
    a1, a2 = pointA
    b1, b2 = pointB
    return(math.sqrt((a1-b1)**2 + (a2-b2)**2))

def circle_rect_collision(circle_pos, circle_radius, rect_list):
    for pipes in rect_list:

        xUp = pipes.x
        yUp = 0
        lUp = pipes.length
        hUp = pipes.top_height
        xDown = pipes.x
        yDown = pipes.top_height + settings.difficulty
        lDown = lUp
        hDown = settings.screenHeigth - yDown
        

        x, y = circle_pos
        xMidUp, yMidUp = xUp + (lUp/2), yUp + (hUp/2)
        xMidDown, yMidDown = xDown + (lDown/2), yDown + (hDown/2)


        # test de collision avec la face gauche du rectangle supérieur
        if (x + settings.player_radius > xMidUp - (lUp / 2)) and (y<hUp) and (x<xUp):
            return(True)
        # test de collision avec la face gauche du rectangle inférieur
        if (x + settings.player_radius > xMidDown - (lDown / 2)) and (y>hUp+settings.difficulty)and (x<xUp):
            return(True)
        # test de collision avec la face basse du rectangle supérieur
        if (y - settings.player_radius < yMidUp + hUp / 2) and (x < xMidUp + lUp / 2) and (x > xMidUp - lUp / 2):
            return (True)
        # test de collision avec la face haute du rectangle inférieur
        if (y + settings.player_radius > yMidDown - hDown / 2) and (x < xMidUp + lUp / 2) and (x > xMidUp - lUp / 2):
            return (True)
        # test de collision avec le sommet gauche du rectangle supérieur
        point = (x,y)
        point2 = (xUp, yUp+hUp)
        if distance(point, point2) < settings.player_radius:
            return(True)
        # test de collision avec le sommet gauche du rectangle inférieur
        point3 = (xDown,yDown)
        if distance(point, point3) < settings.player_radius:
            return(True)
        # test de collision avec le sommet droit du rectangle supérieur
        point4 = (xUp + lUp, yUp+hUp)
        if distance(point, point4) < settings.player_radius:
            return(True)
        # test de collision avec le sommet droit du rectangle inférieur
        point5 = (xDown + lDown, yDown)
        if distance(point, point5) < settings.player_radius:
            return (True)
        # test de collision avec le plafond et le sol
        if (y + circle_radius > settings.ground_level) or (y < 0):
            return(True)

    return (False)

def gameOver(player_pos, pipeMap):  # teste la collision entre un tuyau et l'oiseau
    # ne pas oublier que l'oiseau fait 30 unités de rayon // jsp pq 29 est plus smooth

    # collision avec les bordures supérieures et inférieures de la map
    if player_pos.y < 70  or player_pos.y > settings.screenHeigth - 26:
        return (True)
    
    # collision avec les tuyaux
    # la liste pipeMap n'est jamais vide car on l'initialise, mais elle ne contient pas directement 2 éléments d'où le test sur length :
    if len(pipeMap) == 1:
        if circle_rect_collision((player_pos.x,player_pos.y), settings.player_radius, pipeMap):
            return(True)
    else:
        if circle_rect_collision((player_pos.x,player_pos.y), settings.player_radius, pipeMap[:3]):
            return(True)
    