#stdlib
import random
#3rd party
import pygame 
#local
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0) 

#Overriding the draw method from CircleShape
    def draw(self, surface):
        pygame.draw.circle(
            surface, 
            "white", 
            (int(self.position.x),int(self.position.y)), 
            int(self.radius), 
            LINE_WIDTH, #trailing comma is 'standard' ; no effect at runtime!
            )
    
#This obviously 
    def update(self, dt):
       self.position += (self.velocity * dt)
       self._wrap_position()


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