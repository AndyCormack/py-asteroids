import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TARGET_FRAMERATE
from ui import UI
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    UI.containers = (updatable, drawable)
    UI(screen, player)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    AsteroidField()

    while True:
        # Player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Game state
        for u in updatable:
            u.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                sys.exit(0)

            for shot in shots:
                if asteroid.colliding(shot):
                    asteroid.split()
                    shot.kill()
                    player.add_score()

        # Rendering
        screen.fill(pygame.Color(0, 0, 0))
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(TARGET_FRAMERATE) / 1000


if __name__ == "__main__":
    main()
