import pygame
import sys

# Screen setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Bresenham Line Drawing")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def bresenham(surface, x0, y0, x1, y1, color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    x, y = x0, y0

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            surface.set_at((x, y), color)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            surface.set_at((x, y), color)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx

# Example coordinates
x0, y0 = 100, 100
x1, y1 = 700, 500

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    bresenham(screen, x0, y0, x1, y1, WHITE)
    pygame.display.update()
