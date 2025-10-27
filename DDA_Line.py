import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple DDA Line Drawing")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def dda(surface, x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))

    if steps == 0:
        surface.set_at((int(round(x0)), int(round(y0))), color)
        return

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x0, y0
    for _ in range(steps + 1):
        surface.set_at((int(round(x)), int(round(y))), color)
        x += x_inc
        y += y_inc

# Main loop
x0, y0 = 100, 100
x1, y1 = 500, 400

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    dda(screen, x0, y0, x1, y1, WHITE)
    pygame.display.update()
