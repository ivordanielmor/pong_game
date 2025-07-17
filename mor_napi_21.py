# 21. nap Pong játék
# 1. Ablak és háttér: hozz létre egy 800x600-as pygame ablakot. Háttérszin legyen szürke.

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Pong játék")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     screen.fill((128, 128, 128))
#     pygame.display.update()

# 2. Labda és ütő definiálása
# Definiáld a játékobjektumokat, rajzold ki őket fehér téglalapként minden frame-ben.

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Pong játék")


# WHITE = (255, 255, 255)

# paddle = pygame.Rect(50, 250, 10, 100)

# ball = pygame.Rect(400, 300, 15, 15)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     screen.fill((128, 128, 128))

#     pygame.draw.rect(screen, WHITE, paddle)
#     pygame.draw.rect(screen, WHITE, ball)

#     pygame.display.update()

# 3. ütő mozgatása: A billentyűnyomásokat (UP és DOWN) eseményciklusban
# dolgozd fel. Minden frame-en frissitsd a paddle.y értékét - 
# Ügyelj arra, hogy az ütő ne menjen ki az ablakból!

# import pygame

# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Pong játék")

# WHITE = (255, 255, 255)

# paddle = pygame.Rect(50, 250, 10, 100)
# ball = pygame.Rect(400, 300, 15, 15)

# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP] and paddle.top > 0:
#         paddle.y -= 5
#     if keys[pygame.K_DOWN] and paddle.bottom < 600:
#         paddle.y += 5

#     screen.fill((128, 128, 128))
#     pygame.draw.rect(screen, WHITE, paddle)
#     pygame.draw.rect(screen, WHITE, ball)

#     pygame.display.update()
#     clock.tick(60)

# 4. feladat: Bővités: paraméterek konstansként,
# Célszerű az ablakméretet, ütőméretet és szineket a kód elején,
# nagybetűs változókban tárolni.

# import pygame

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
# BALL_SIZE = 15
# WHITE = (255, 255, 255)
# GRAY = (128, 128, 128)
# PADDLE_SPEED = 5
# FPS = 60

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Pong játék")

# paddle = pygame.Rect(50, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
# ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP] and paddle.top > 0:
#         paddle.y -= PADDLE_SPEED
#     if keys[pygame.K_DOWN] and paddle.bottom < HEIGHT:
#         paddle.y += PADDLE_SPEED

#     screen.fill(GRAY)
#     pygame.draw.rect(screen, WHITE, paddle)
#     pygame.draw.rect(screen, WHITE, ball)

#     pygame.display.update()
#     clock.tick(FPS)

# HÁZI FELADAT: - Duplázd meg a pálya szélén a másik ütőt(jobb oldalon),
# és mozgasd "W/S" billentyűkkel! - Állitsd be, hogy ha az ütő fent vagy 
# lent eléri a képernyő szélét, ne szaladjon tovább.
# - (Extra): Rajzold ki a labdát is (egy 20x20-as fehér téglalapként), még
# ha nem mozog, csak legyen látható! 

# import pygame

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
# BALL_SIZE = 20
# WHITE = (255, 255, 255)
# GRAY = (128, 128, 128)
# PADDLE_SPEED = 5
# FPS = 60

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Pong játék")

# paddle_left = pygame.Rect(50, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# paddle_right = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_w] and paddle_left.top > 0:
#         paddle_left.y -= PADDLE_SPEED
#     if keys[pygame.K_s] and paddle_left.bottom < HEIGHT:
#         paddle_left.y += PADDLE_SPEED

#     if keys[pygame.K_UP] and paddle_right.top > 0:
#         paddle_right.y -= PADDLE_SPEED
#     if keys[pygame.K_DOWN] and paddle_right.bottom < HEIGHT:
#         paddle_right.y += PADDLE_SPEED

#     screen.fill(GRAY)

#     pygame.draw.rect(screen, WHITE, paddle_left)
#     pygame.draw.rect(screen, WHITE, paddle_right)
#     pygame.draw.rect(screen, WHITE, ball)

#     pygame.display.update()
#     clock.tick(FPS)
