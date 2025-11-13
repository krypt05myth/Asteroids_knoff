import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, SHIP_TURN_SPEED

#Player inherits directly from CircleShape
class Player(CircleShape):
    #Player constructor uses x and y
    def __init__(self, x, y):
        #CircleShape uses x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
# in the Player class
# A player will look like a triangle, even though we'll use a circle to represent its hitbox. 
# The math of drawing a triangle can be a bit tricky, so we've written the method for you
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
#Overriding the draw method and it calls the draw.polygon method from pygame
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
#Rotates the player's by the relative fraction of the const to dt; ie dt=1/60 so 1/60th of const or const/60
    def rotate(self, dt):
        self.rotation += (SHIP_TURN_SPEED * dt)
#
    def update(self, dt):
        keys = pygame.key.get_pressed()
#K_a is apparently rotating left?
        if keys[pygame.K_a]:
            self.rotate(dt*(-1))
        if keys[pygame.K_d]:
            self.rotate(dt)