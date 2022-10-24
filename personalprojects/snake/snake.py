import pygame
import time

pygame.init()
dis=pygame.display.set_mode((800,800))
green=(0,255,0)
pygame.display.set_caption('Snake by Shatterdest')
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
    pygame.display.update()
    pygame.draw.rect(dis,green,[400,400,10,10])
pygame.quit()
quit()