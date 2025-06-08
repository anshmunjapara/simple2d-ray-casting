import pygame


class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.start = pygame.math.Vector2(x1, y1)
        self.end = pygame.math.Vector2(x2, y2)

    def show(self, surface):
        pygame.draw.aaline(surface, (255, 255, 255), self.start, self.end)

    def wall_to_wall_intersection(self, wall2):
        x1, y1 = self.start
        x2, y2 = self.end
        x3, y3 = wall2.start
        x4, y4 = wall2.end

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom

        if 0 <= t <= 1 and 0 <= u <= 1:
            intersection = pygame.math.Vector2(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
            return intersection
        return None
