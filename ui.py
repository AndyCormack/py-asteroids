import pygame
import pygame.freetype
from constants import WHITE
from player import Player


class UI(pygame.sprite.Sprite):
    def __init__(self, screen, player: Player):
        super().__init__(self.containers)
        self.font = pygame.freetype.Font(None, 36)
        self.player = player

    def draw(self, screen: pygame.Surface):
        self.font.render_to(screen, (20, 20), f"Score: {self.player.score}", WHITE)
