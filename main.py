import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0
#Holds Group and Containers objects 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group() 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

#Instantiating Player with x y values
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)
#Instantiating AsteroidField
    asteroid_field = AsteroidField()
#Main game loop runs until "X (close_click)" or "ctrl-c"
    while running:
        log_state()
#"wipes" the previous frame
        screen.fill("black")
#draws/redraws the player's ship
        for ea_drawable in drawable:
            ea_drawable.draw(screen)
#factor in rotation before final rendering
        updatable.update(dt)

        for ea_asteroid in asteroids:
            if ea_asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for ea_shot in shots:
                if ea_shot.collides_with(ea_asteroid):
                    log_event("asteroid_shot")
                    ea_shot.kill()
                    ea_asteroid.split()

#shows/renders the new 'imaged'
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dt = clock.tick(60)/1000
           # testing the above works as intended
        #print(f"Delta time: {dt}")
        
    pygame.quit()

if __name__ == "__main__":
    main()
