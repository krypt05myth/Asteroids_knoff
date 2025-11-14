#3rd party
import pygame
#local
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

#Takes itself and another Circle
    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        min_collide_distance = self.radius + other.radius
        if distance <= min_collide_distance:
            return True
        return False
    
#Totally gratuitous to the requirement...
# Wraps asteroids and player back around to opposite side when exceeding screen/frame bounds
    def _wrap_position(self):
        if self.position.x < 0: self.position.x += SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH: self.position.x -= SCREEN_WIDTH
        if self.position.y < 0: self.position.y += SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT: self.position.y -= SCREEN_HEIGHT