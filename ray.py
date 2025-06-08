import pygame.math


class Ray:
    def __init__(self, origin, angle):
        self.origin = origin
        self.dir = pygame.math.Vector2(0, 1).rotate(angle)
        self.length = 10

    def show(self, surface):
        pygame.draw.aaline(surface, (255, 255, 255), self.origin, self.origin + self.dir * self.length)

    def update(self, pos):
        self.dir.x = pos[0] - self.origin[0]
        self.dir.y = pos[1] - self.origin[1]
        self.dir.normalize_ip()

    def cast(self, wall):
        x1, y1 = wall.start
        x2, y2 = wall.end
        x3, y3 = self.origin
        x4, y4 = self.origin + self.dir

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom

        if 0 <= t <= 1 and u >= 0:
            intersection = pygame.math.Vector2(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
            return intersection
        return None
