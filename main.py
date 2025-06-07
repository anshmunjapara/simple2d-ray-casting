import pygame


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

    # Example: draw a red circle
    pygame.draw.circle(screen, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), 50)

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()

