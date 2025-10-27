import pygame, sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Kite Animation")
clock = pygame.time.Clock()

SKY_BLUE = (135, 206, 235)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

x = 50
y = 200
speed = 4


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += speed

    if x > WIDTH - 30 or x < 30:
        speed = -speed

    screen.fill(SKY_BLUE)

    pygame.draw.circle(screen, RED, (x, y), 30)

    pygame.draw.line(screen, WHITE, (x, y+30), (WIDTH // 2, HEIGHT), 2)

    pygame.display.flip()
    clock.tick(60)
