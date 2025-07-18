# 4. feladat: Bővités: paraméterek konstansként,
# Célszerű az ablakméretet, ütőméretet és szineket a kód elején,
# nagybetűs változókban tárolni.

import pygame

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
WHITE = (255, 255, 255)
GRAY = (28, 28, 28)
PADDLE_SPEED = 5
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong játék")

paddle = pygame.Rect(50, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle.bottom < HEIGHT:
        paddle.y += PADDLE_SPEED

    screen.fill(GRAY)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.rect(screen, WHITE, ball)

    pygame.display.update()
    clock.tick(FPS)
    