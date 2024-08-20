import map
import collision
import settings
import pygame
import brain
import random

class Player:
    def __init__(self):
        # Bird
        self.pos = pygame.Vector2(settings.player_spawnpoint)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.body = settings.player_radius
        self.speed = 0
        self.flap = False
        self.alive = True
        self.lifespan = 0
        
        # AI
        self.decision = None
        self.vision = [0.5, 1, 0.5]
        self.fitness = 0
        self.inputs = 3
        self.brain = brain.Brain(self.inputs)
        self.brain.generate_net()

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.pos, self.body)

    def collision(self):
        return(collision.gameOver(self.pos,map.pipes))
    
    def update(self):
        if not self.collision():  # actualisation du mouvement
            # Gravity
            self.speed += settings.g
            self.pos.y += self.speed
            if self.speed > 5:
                self.speed = 5
            # Increment lifespan
            self.lifespan += 1
        else:
            self.alive = False
            self.flap = False
            self.speed = 0

    def bird_flap(self):
        if not self.flap :
            self.flap = True
            self.speed = settings.j
        if self.speed >= settings.jump_rate:
            self.flap = False
    
    @staticmethod
    def closest_pipe():
        for p in map.pipes:
            if not p.passed:
                return p
    
    # AI related functions
    def look(self,window):
        if map.pipes:

            # Line to top pipe
            self.vision[0] = max(0, self.pos.y - self.closest_pipe().top_rect.bottom) / 500

            # Line to mid pipe
            self.vision[1] = max(0, self.closest_pipe().x - self.pos.x) / 500

            # Line to bottom pipe
            self.vision[2] = max(0, self.closest_pipe().bottom_rect.top - self.pos.y) / 500

    def calculate_fitness(self):
        self.fitness = self.lifespan

    def clone(self):
        clone = Player()
        clone.fitness = self.fitness
        clone.brain = self.brain.clone()
        clone.brain.generate_net()
        return clone

    def think(self):
        self.decision = self.brain.feed_forward(self.vision)
        if self.decision > 0.73:
            self.bird_flap()