import pygame 
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0) 

#Overriding the draw method: it calls the draw.circle method from pygame
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
    
#This obviously 
    def update(self, dt):
       self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velo_1 = self.velocity.rotate(random_angle)
        velo_2 = self.velocity.rotate(-random_angle)
        aster_1 = Asteroid(self.position.x, self.position.y, new_radius)
        aster_1.velocity = velo_1 * 1.2
        aster_2 = Asteroid(self.position.x, self.position.y, new_radius)
        aster_2.velocity = velo_2 * 1.2
