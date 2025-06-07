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
    # Wall(700, 200, 700, 300)
for _ in range(5):
    x1 = random.randint(0, WIDTH)
    y1 = random.randint(0, HEIGHT)
    x2 = random.randint(0, WIDTH)
    y2 = random.randint(0, HEIGHT)
    walls.append(Wall(x1, y1, x2, y2))

lightSource = Light(400, 300)

# Main game loop
running = True

while running:
    clock.tick(FPS)  # Limit FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here
    mouse_pos = pygame.mouse.get_pos()
    lightSource.update(mouse_pos[0], mouse_pos[1])


    # Drawing
    screen.fill(BG_COLOR)
    for wall in walls:
        wall.show(screen)

    lightSource.cast(screen, walls[0])
    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
