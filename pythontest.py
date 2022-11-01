
import random
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
def is_white(i,j):
    return (i+j)%2==0
width = 20
height = 20
red = 255
green = 255
blue = 255
Blanc = [255, 255, 255]
Noir = [0,0,0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    for i in range(30):
        x=20*i
        for j in range (30):
            y=20*j
            if (i+j)%2==0:
                rect = [x, y, width, height]
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                color = [red, green, blue]
                pygame.draw.rect(screen, color, rect)
            pygame.display.update()
            clock.tick(0)

    
    





    
'''while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                print("↑")
            if event.key == pygame.K_DOWN:
                print("↓")
            if event.key == pygame.K_LEFT:
                print("←") 
            if event.key == pygame.K_RIGHT:
                print("→")           
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = [red, green, blue]
    screen.fill(color)
    pygame.display.update()
    clock.tick(99999)'''


