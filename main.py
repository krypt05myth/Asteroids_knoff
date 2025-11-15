#stdlib
import sys
#3rd party
import pygame
#local
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from shot import Shot

def main():
    pygame.init()
    version = pygame.version.ver    #Why was this needed?

#TODO: might we later upgrade to in game window temp notifications
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

 #Generic variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Creates static game play area
    running = True  #Will be flipped/handled upon any exit event
    clock = pygame.time.Clock() #
    dt = 0  #Delta Time, updated at end of main game while loop

#Holds Group and Containers objects 
# Mental model

# “containers” = “which groups should this sprite auto-join when constructed?”
# “groups” = “buckets that let me update/draw/check collisions in bulk.”

# sprite groups
    asteroids = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
# container wiring
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

# entities 
    x = SCREEN_WIDTH//2 #instead of /, to keep integer instead of float
    y = SCREEN_HEIGHT//2    #reduces "sub-pixel" blurring aka "off-by-one" rendering issues
    player = Player(x, y)
    asteroid_field = AsteroidField()

#Main game loop runs until "X (close_click)" or "ctrl-c"
    while running:
        log_state()
    #handling exit/quit events to kill while loop
    # having these first reduces input latency - game reacts before going thru frame refresh stuff
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    #factor in rotation before final rendering
    # update-then-draw so that what is drawn is latest intead of one frame behind!
        updatable.update(dt)    
        
    #"wipes" the previous frame
        screen.fill("black")
    #draws/redraws the player's ship
        for d in drawable:
            d.draw(screen)
    #shows/renders the new 'imaged'
        pygame.display.flip()   
    
    #check for collisions with playere or with player's shots, handle accordingly
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()

        dt = clock.tick(60)/1000
        
    pygame.quit()

if __name__ == "__main__":
    main()