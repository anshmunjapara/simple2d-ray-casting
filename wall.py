import pygame


class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.start = pygame.math.Vector2(x1, y1)
        self.end = pygame.math.Vector2(x2, y2)

    def show(self, surface):
        pygame.draw.aaline(surface, (255, 255, 255), self.start, self.end)
