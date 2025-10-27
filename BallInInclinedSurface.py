import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rolling Ball on Inclined Plane")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREY = (180, 180, 180)
RED = (255, 0, 0)

x = 100
y = 100
radius = 25
speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += speed
    y += 1.2 

    if x > 700:
        x = 700
        y = 600

    screen.fill(WHITE)
    pygame.draw.line(screen, GREY, (100, 100), (700, 500), 5)

    pygame.draw.circle(screen, RED, (int(x)+20, int(y)), radius)
    pygame.draw.polygon(screen, (0,255,0), [(100,100), (700,500), (100,500)])

    pygame.display.update()
    clock.tick(60)
