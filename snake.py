import random
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()


def is_white(i, j):
    return (i + j) % 2 == 0


width = 20
height = 20
Blanc = [255, 255, 255]
Noir = [0, 0, 0]
Rouge = [255, 0, 0]
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = [1, 0]

fruit = [random.randint(0, 29), random.randint(0, 29)]
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_DOWN and direction != [0, -1]:
                direction = [0, 1]
            if event.key == pygame.K_UP and direction != [0, 1]:
                direction = [0, -1]
            if event.key == pygame.K_LEFT and direction != [1, 0]:
                direction = [-1, 0]
            if event.key == pygame.K_RIGHT and direction != [-1, 0]:
                direction = [1, 0]

    tete = snake[-1]
    tete2 = [tete[0] + direction[0], tete[1] + direction[1]]
    if tete2 in snake:
        pygame.quit()
        sys.exit()
    snake.append(tete2)
    snake.pop(0)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = [red, green, blue]
    for i in range(30):
        x = 20 * i
        for j in range(30):
            y = 20 * j
            rect = [x, y, width, height]
            
            pygame.draw.rect(screen, Blanc, rect)

    for part in snake:
        rect = [part[0] * 20, part[1] * 20, width, height]
        pygame.draw.rect(screen, Noir, rect)

    rectf = [fruit[0] * 20, fruit[1] * 20, width, height]
    pygame.draw.rect(screen, Rouge, rectf)

    if tete2 == fruit:
        fruit = [random.randint(0, 29), random.randint(0, 29)]
        snake = snake + [tete2]
        score += 10
    if snake[-1][0] > 30 or snake[-1][0] < 0 or snake[-1][1] > 30 or snake[-1][1] < 0:
        pygame.quit()
        sys.exit()
    if fruit in snake:
        fruit = [random.randint(0, 29), random.randint(0, 29)]
    pygame.display.set_caption(f"🐍 Score: {score}")
    pygame.display.update()
    clock.tick(3)
