# # 1. Ablak és háttér: hozz létre egy 800x600-as pygame ablakot. Háttérszin legyen szürke.

import pygame

WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong játék")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((28, 28, 28))
    pygame.display.update()