import random
import pygame
import sys

# Constantes
WIDTH = 30 # number of cells
HEIGHT = 30 # number of cells
CELL_SIZE = 20 # number of pixels
FPS=3  # frames per second
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
COLORS = {
    "background": WHITE,
    "snake": BLACK,
    "fruit": RED
}
UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

#Setup
pygame.init()
screen = pygame.display.set_mode([WIDTH*CELL_SIZE, HEIGHT*CELL_SIZE])
clock = pygame.time.Clock()
def exit():
    pygame.quit()
    sys.exit()

#Initial variables
snake = [
    [10, 15],
    [11, 15],
    [12, 15],
]
direction = RIGHT 
fruit = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]
score = 0

# Main loop
while True:

#Event Management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
#Game State
            if event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            if event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

#Game Logic (move snake)
    tete = snake[-1]
    tete2 = [tete[0] + direction[0], tete[1] + direction[1]]
    if tete2 in snake or snake[-1][0] > WIDTH-1 or snake[-1][0] < 0 or snake[-1][1] > HEIGHT-1 or snake[-1][1] < 0:
        exit()
    snake.append(tete2)
    snake.pop(0)


#Game Logic (fruit)
    if tete2 == fruit:
        snake = snake + [tete2]
        score += 10
        fruit = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]
    if fruit in snake:
        fruit = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]
        

#Frame Update
    for i in range(WIDTH):
        x = CELL_SIZE * i
        for j in range(HEIGHT):
            y = CELL_SIZE * j
            rect = [x, y, CELL_SIZE, CELL_SIZE]
            #red = random.randint(0, 255)
            #green = random.randint(0, 255)
            #blue = random.randint(0, 255)
            #color = [red, green, blue]
            pygame.draw.rect(screen, COLORS["background"], rect)
    for part in snake:
        rect = [part[0] * CELL_SIZE, part[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE]
        pygame.draw.rect(screen, COLORS["snake"], rect)
    rectf = [fruit[0] * CELL_SIZE, fruit[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE]
    pygame.draw.rect(screen, COLORS["fruit"], rectf)
    pygame.display.set_caption(f"🐍 Score: {score}")
    pygame.display.update()
    clock.tick(FPS)
