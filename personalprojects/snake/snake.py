import random
import pygame
import time

pygame.init()
dis_width=800
dis_length=800
dis=pygame.display.set_mode((dis_length,dis_width))
green=(0,255,0)
black=(0,0,0)
red = (255, 0, 0)
blue = (0, 0, 255)

snake_speed = 30
snake_block=10
font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_length/3])

clock = pygame.time.Clock()

pygame.display.set_caption('Snake by Shatterdest')
def gameLoop():
    x1 = dis_width/2
    y1 = dis_length/2

    x1_change = 0
    y1_change = 0
    
    game_over = False
    game_close = False
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    while not game_over:
        
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again",red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    x1_change = -10
                    y1_change = 0
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    x1_change = 10
                    y1_change = 0
                elif event.key in (pygame.K_UP, pygame.K_w):
                    y1_change = -10
                    x1_change = 0
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    y1_change = 10
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_length or y1 < 0:
            game_over = True
        pygame.display.update()
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.display.update()
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, green, [x1, y1, snake_block, snake_block])
        clock.tick(snake_speed)


    time.sleep(2)

    pygame.quit()
    quit()

gameLoop()