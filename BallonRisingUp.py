import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Single Balloon Rising")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 400
y = 550
radius = 25
speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if y > -radius:
        y -= speed

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, RED, (int(x), int(y)), radius)
    pygame.draw.line(screen, WHITE, (int(x), int(y) + 25), (int(x), int(y) + 100), 2)

    pygame.display.update()
    clock.tick(60)
