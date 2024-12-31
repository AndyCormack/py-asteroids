import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        # Player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Game state

        # Rendering
        screen.fill(pygame.Color(0,0,0))
        # Render stuff
        pygame.display.flip()
        dt = clock.tick(TARGET_FRAMERATE) / 1000

if __name__ == "__main__":
    main()
