import math

import pygame.math

from ray import Ray

ALPHA = 0.0001


class Light:
    def __init__(self, x, y):
        self.position = pygame.math.Vector2(x, y)
        self.a = 1
        self.rays = []

        # for i in range(0, 360, self.a):
        #     self.rays.append(Ray(self.position, i))

    def update(self, x, y):
        self.position.x = x
        self.position.y = y

    def update_rays(self, walls):
        self.rays.clear()
        for wall in walls:
            for point in [wall.start, wall.end]:
                print(point)
                angle = math.degrees(math.atan2(point.y - self.position.y, point.x - self.position.x))
                angle -= 90
                for delta in [-ALPHA, 0, ALPHA]:
                    self.rays.append(Ray(self.position, angle + delta))

    def cast(self, surface, walls):

        self.update_rays(walls)

        ray_surf = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
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
                print(f"{minPt} for the ray : {ray.dir}")
                pygame.draw.aaline(ray_surf, (255, 219, 77, 150), ray.origin, minPt)

        surface.blit(ray_surf, (0, 0))
