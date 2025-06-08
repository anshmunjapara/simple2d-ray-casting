import random

import pygame
import pygame.gfxdraw

from light import Light
from ray import Ray
from wall import Wall

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (30, 30, 30)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Clock for controlling frame rate
clock = pygame.time.Clock()

walls = []

for _ in range(5):
    x1 = random.randint(0, WIDTH)
    y1 = random.randint(0, HEIGHT)
    x2 = random.randint(0, WIDTH)
    y2 = random.randint(0, HEIGHT)
    walls.append(Wall(x1, y1, x2, y2))

walls.append(Wall(0, 0, WIDTH, 0))
walls.append(Wall(WIDTH, 0, WIDTH, HEIGHT))
walls.append(Wall(WIDTH, HEIGHT, 0, HEIGHT))
walls.append(Wall(0, HEIGHT, 0, 0))

lightSource = Light(400, 300)

drawing_wall = False
wall_start = None

# Main game loop
running = True

while running:
    clock.tick(FPS)  # Limit FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            keys = pygame.key.get_mods()
            if keys & pygame.KMOD_SHIFT:
                if not drawing_wall:
                    wall_start = pygame.mouse.get_pos()
                    drawing_wall = True
                else:
                    wall_end = pygame.mouse.get_pos()
                    walls.append(Wall(wall_start[0], wall_start[1], wall_end[0], wall_end[1]))
                    drawing_wall = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right click
            drawing_wall = False
            wall_start = None
    # Game logic goes here
    mouse_pos = pygame.mouse.get_pos()
    lightSource.update(mouse_pos[0], mouse_pos[1])

    # Drawing
    screen.fill(BG_COLOR)
    for wall in walls:
        wall.show(screen)

    if drawing_wall and wall_start:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, (100, 255, 100), wall_start, mouse_pos, 2)

    if not drawing_wall:
        lightSource.cast(screen, walls)
    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
