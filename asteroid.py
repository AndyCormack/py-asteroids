import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, WHITE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        radius = self.radius - ASTEROID_MIN_RADIUS
        if radius < ASTEROID_MIN_RADIUS:
            return

        direction = random.uniform(20, 50)
        velocity = [self.velocity.rotate(direction), self.velocity.rotate(-direction)]
        radius = self.radius - ASTEROID_MIN_RADIUS

        for v in velocity:
            asteroid = Asteroid(self.position.x, self.position.y, radius)
            asteroid.velocity = v
