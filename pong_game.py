# 3. ütő mozgatása: A billentyűnyomásokat (UP és DOWN) eseményciklusban
# dolgozd fel. Minden frame-en frissitsd a paddle.y értékét - 
# Ügyelj arra, hogy az ütő ne menjen ki az ablakból!

import pygame

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong játék")

paddle = pygame.Rect(50, 250, 10, 100)
ball = pygame.Rect(400, 300, 15, 15)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.y -= 5
    if keys[pygame.K_DOWN] and paddle.bottom < 600:
        paddle.y += 5

    screen.fill(GRAY)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.rect(screen, WHITE, ball)

    pygame.display.update()
    clock.tick(60)