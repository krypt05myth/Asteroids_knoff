import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, LINE_WIDTH, SHIP_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED

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
#Overriding the draw method: it calls the draw.polygon method from pygame
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
#Rotates the player's by the relative fraction of the const to dt; ie dt=1/60 so 1/60th of const or const/60
    def rotate(self, dt):
        self.rotation += (SHIP_TURN_SPEED * dt)
#This obviously takes key presses for doin the rotates
    def update(self, dt):
        keys = pygame.key.get_pressed()
        #K_a is apparently rotating left? ... must be == keyboard_a{key}
        if keys[pygame.K_a]:
            self.rotate(dt*(-1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*(-1))
        if keys[pygame.K_SPACE]:
            self.shoot()
#Vector math to carry out the player's moves
    def move(self, dt):
        #1. Draw a unit vector pointing straight up from 0,0 to 0,1
        unit_vector = pygame.Vector2(0, 1)
        #2. Rotate vector sideways by player's rotation so it's pointing in the same direction as player 
        rotated_vector = unit_vector.rotate(self.rotation)
        #3. Adjust the speed to the length the player should move during the frame
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        #4. Move the player by adding the vector to the player's position
        self.position += rotated_with_speed_vector
#
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot_vector = pygame.Vector2(0, 1)
        rot_vector = shot_vector.rotate(self.rotation)
        shot.velocity = rot_vector * PLAYER_SHOOT_SPEED
