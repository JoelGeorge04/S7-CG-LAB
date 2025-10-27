import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Animation")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)

x = 400
y =  200
radius = 30
speed = 5  


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    y += speed
    if y > HEIGHT - radius or y < 30:
        speed = -speed  

    screen.fill(BLACK)

    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()

    clock.tick(60)
