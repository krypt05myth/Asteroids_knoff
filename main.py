import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0
#Instantiating Player with x y values
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)

#Main game loop runs until "X (close_click)" or "ctrl-c"
    while running:
        log_state()
#"wipes" the previous frame
        screen.fill("black")
#draws/redraws the player's ship
        player.draw(screen)
#factor in rotation before final rendering
        player.update(dt)
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
