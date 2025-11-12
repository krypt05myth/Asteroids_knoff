import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    VERSION = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        log_state()
        screen.fill("black")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()
