import pygame 
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
#Overriding the draw method: it calls the draw.circle method from pygame
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
    
#This obviously 
    def update(self, dt):
       self.position += (self.velocity * dt)