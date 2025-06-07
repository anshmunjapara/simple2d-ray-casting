import pygame

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

wall = Wall(700, 200, 700, 300)

ray = Ray((200, 250), 90)

# Main game loop
running = True

while running:
    clock.tick(FPS)  # Limit FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Drawing
    screen.fill(BG_COLOR)
    wall.show(screen)
    ray.show(screen)
    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
