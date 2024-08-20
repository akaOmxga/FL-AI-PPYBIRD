import pygame
from sys import exit
import settings
import map
import population

################################################################### SETTINGS ###################################################################

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption(settings.titre)
font = pygame.font.Font(None, 36)
# delta time
dt = clock.tick(settings.fps) / 1000 # temps écoulé depuis la dernière frame lorsque l'on update le jeu à 120 fps

# écran de jeu
window = pygame.display.set_mode((settings.screenLength, settings.screenHeigth))

# population de bird
population = population.Population(settings.size)

################################################################### FONCTION ###################################################################

def spawn_pipes():
    map.pipes.append(map.Pipes())

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

################################################################### MAIN LOOP ###################################################################

def main():
    while True:
        # vérification de la fermeture du jeu
        quit_game()

        # fond d'écran bleu ciel flappy bird
        window.fill(settings.background_color)

        # faire apparaître le sol
        map.sol.draw(window)

        # faire apparaître et actualiser les tuyaux 
        xNewElement = settings.screenLength - settings.pipeDistance
        if map.pipes == []:
            spawn_pipes()
        else :
            xLast = map.pipes[-1].x
            if xLast < xNewElement:
                spawn_pipes()
        for p in map.pipes:
            p.draw(window)
            p.update(dt)
            if p.off_screen:
                map.pipes.remove(p)

        # update les joueurs 
        if not population.extinct():
            population.update_live_players(window)
        else:
            map.pipes.clear()
            population.natural_selection()

        # affichage des points et de la génération :
        # affichage des points : 
        text = font.render(str(population.generation_point), True,"black")
        text_rect = text.get_rect()
        text_rect.center = (window.get_width() / 2, window.get_height() / 10)
        # dessiner les points
        window.blit(text, text_rect)
        # affichage de la génération : 
        gen = population.generation
        text = font.render("gen. n° : " + str(gen), True,"black")
        text_rect = text.get_rect()
        text_rect.center = (window.get_width() / 10, window.get_height() / 10)
        # dessiner la génération 
        window.blit(text, text_rect)


        # actualiser l'écran
        clock.tick(settings.fps)
        pygame.display.flip()


### appel de la fonction main
main()