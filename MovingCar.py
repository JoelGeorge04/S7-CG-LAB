import pygame, sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Animation")

SKY_BLUE = (135, 206, 235)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

x = 50
y = 450
speed = 4

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += speed
    if x > WIDTH - 50 or x < 50:
        speed = -speed

    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 100, WIDTH, 100))

    car_points = [
        (x + 40, y),
        (x - 40, y),
        (x - 40, y + 30),
        (x + 40, y + 30)
    ]
    pygame.draw.polygon(screen, RED, car_points)
    pygame.draw.circle(screen, BLACK, (x - 25, y + 35), 10)
    pygame.draw.circle(screen, BLACK, (x + 25, y + 35), 10)

    pygame.display.flip()
    clock.tick(60)
