#3rd party
import pygame
#local
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, surface):
        #this is how I originally did it - here and everywhere similar, too --v
        # pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
        #Bootsy been recomm --v
        pygame.draw.circle(
            surface,
            "white",
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            LINE_WIDTH,
        )
    
#This obviously 
    def update(self, dt):
       self.position += (self.velocity * dt)
       #silly, and fun to turn on, but not required!
       # self._wrap_position()