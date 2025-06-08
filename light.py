import pygame.math

from ray import Ray


class Light:
    def __init__(self, x, y):
        self.position = pygame.math.Vector2(x, y)
        self.a = 1
        self.rays = []
        for i in range(0, 360, self.a):
            self.rays.append(Ray(self.position, i))

    def update(self, x, y):
        self.position.x = x
        self.position.y = y

    def cast(self, surface, walls):
        for ray in self.rays:
            ray.show(surface)

        for ray in self.rays:
            minDistance = float('inf')
            minPt = None
            for wall in walls:
                pt = ray.cast(wall)
                if pt:
                    dis = self.position.distance_to(pt)
                    if dis < minDistance:
                        minDistance = dis
                        minPt = pt
            if minPt:
                pygame.draw.aaline(surface, (255, 255, 255), ray.origin, minPt)



