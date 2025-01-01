import pygame
import pygame.freetype
from constants import WHITE


class UI(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__(self.containers)
        self.font = pygame.freetype.Font(None, 36)
        self.stats = {
            "score": 0,
        }

    def draw(self, screen: pygame.Surface):
        self.font.render_to(screen, (20, 20), f"Score: {self.stats['score']}", WHITE)

    def updateScore(self, score):
        self.stats["score"] = score
