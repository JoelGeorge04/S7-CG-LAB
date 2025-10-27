import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Midpoint Circle Drawing")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_points(surface, xc, yc, x, y, color):
    surface.set_at((xc + x, yc + y), color)
    surface.set_at((xc - x, yc + y), color)
    surface.set_at((xc + x, yc - y), color)
    surface.set_at((xc - x, yc - y), color)
    surface.set_at((xc + y, yc + x), color)
    surface.set_at((xc - y, yc + x), color)
    surface.set_at((xc + y, yc - x), color)
    surface.set_at((xc - y, yc - x), color)

def midpoint_circle(surface, xc, yc, r, color):
    x = 0
    y = r
    p = 1 - r
    draw_points(surface, xc, yc, x, y, color)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p +=  2 * (x - y) + 1
        draw_points(surface, xc, yc, x, y, color)

# circle parameters
xc, yc = 400, 300   
r = 150             

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    midpoint_circle(screen, xc, yc, r, WHITE)
    pygame.display.update()
