import pygame
from circleshape import CircleShape
from constants import (
    WHITE,
    RED,
    PLAYER_LIVES,
    PLAYER_INVULNERABILITY,
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.spawn_location = pygame.Vector2(x, y)
        self.rotation = 0
        self.shot_timer = 0
        self.score = 0
        self.lives = PLAYER_LIVES
        self.invulnerability = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = self.invulnerability > 0 and RED or WHITE
        pygame.draw.polygon(screen, color, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.shot_timer <= 0:
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            Shot(self.position.x, self.position.y, forward * PLAYER_SHOOT_SPEED)

    def add_score(self):
        self.score += 1

    def die(self):
        if self.invulnerability > 0:
            return

        if self.lives > 0:
            self.lives -= 1
            self.respawn()

    def respawn(self):
        self.invulnerability = PLAYER_INVULNERABILITY
        self.position = self.spawn_location.copy()

    def update(self, dt):
        if self.shot_timer > 0:
            self.shot_timer -= dt

        if self.invulnerability > 0:
            self.invulnerability -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)
