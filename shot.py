import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
    
#This obviously 
    def update(self, dt):
       self.position += (self.velocity * dt)
    