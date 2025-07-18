# HÁZI FELADAT
# • Adj pontszámlálót: minden alkalommal, amikor a labda kimegy a jobb vagy bal oldalról, növeld a pontot, és jelenítsd meg a képernyő tetején!
# • Próbáld ki különböző dx, dy értékekkel – hogyan változik a játék nehézsége?

import pygame

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
WHITE = (255, 255, 255)
GRAY = (28, 28, 28)
PADDLE_SPEED = 5
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong játék")

paddle_left = pygame.Rect(50, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_right = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

dx, dy = 4, 4
speed_increment = 1.02

clock = pygame.time.Clock()

score_left = 0
score_right = 0

font = pygame.font.SysFont(None, 48)

def reset_ball():
    global dx, dy
    ball.center = (WIDTH // 2, HEIGHT // 2)
    dx = 4 * (1 if dx > 0 else -1)
    dy = 4 * (1 if dy > 0 else -1)

reset_ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and paddle_left.top > 0:
        paddle_left.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_left.bottom < HEIGHT:
        paddle_left.y += PADDLE_SPEED

    if keys[pygame.K_UP] and paddle_right.top > 0:
        paddle_right.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_right.bottom < HEIGHT:
        paddle_right.y += PADDLE_SPEED

    ball.x += dx
    ball.y += dy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        dy = -dy

    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        dx = -dx

    if ball.left <= 0:
        score_right += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        dx = -abs(dx) * speed_increment
        dy = dy * speed_increment

    if ball.right >= WIDTH:
        score_left += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        dx = abs(dx) * speed_increment
        dy = dy * speed_increment

    screen.fill(GRAY)

    pygame.draw.rect(screen, WHITE, paddle_left)
    pygame.draw.rect(screen, WHITE, paddle_right)
    pygame.draw.rect(screen, WHITE, ball)

    score_text = font.render(f"{score_left} : {score_right}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.update()
    clock.tick(FPS)
