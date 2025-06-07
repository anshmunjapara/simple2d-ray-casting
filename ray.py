import pygame.math


class Ray:
    def __init__(self, origin, angle):
        self.origin = origin
        self.dir = pygame.math.Vector2(0, 1).rotate(angle)
        self.length = 10

    def show(self, surface):

        pygame.draw.line(surface, (255, 255, 255), self.origin, self.origin + self.dir*self.length, 2)

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
            print("colide at")
            return intersection
        return None
