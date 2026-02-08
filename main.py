import pygame
import sys
import time
import random

pygame.init()
width = 600
height = 600
snake_speed = 25

snake = (0,255,0)
food = (217, 165, 33)
poison = (255,0,0)
field = (0,0,0 )
messageFall = (255,0,0)
score_color = (255,255,255)

snake_headx_pos = width/2
snake_heady_pos = height/2
snake_blok = 30
score = 0

last_down = None
x_new = 0
y_new = 0
food_x_pos = round(random.randint(0, width - snake_blok)/10.0)*10.0
food_y_pos = round(random.randint(0, height - snake_blok)/10.0)*10.0
snake_List = []
Length_of_snake = 1

poison_x_pos = round(random.randint(0, width - snake_blok)/10.0)*10.0
poison_y_pos = round(random.randint(0, height - snake_blok)/10.0)*10.0

fps = pygame.time.Clock()
first_time = pygame.time.get_ticks()

dis = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
game_over = False

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_blok, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake, [x[0], x[1], snake_blok, snake_blok])

def gameOvermsg(msg, color):
    message = font_style.render(msg, True, color)
    dis.blit(message, [200, 300])

def user_score(score):
    value = score_font.render("Счёт: " + str(score), True, score_color)
    dis.blit(value,[0,0])
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_LEFT and last_down != "right":
                x_new = -10
                y_new = 0
                last_down = "left"
            elif event.key == pygame.K_RIGHT and last_down != "left":
                x_new = 10
                y_new = 0
                last_down = "right"
            elif event.key == pygame.K_UP and last_down != "down":
                x_new = 0
                y_new = -10
                last_down = "up"
            elif event.key == pygame.K_DOWN and last_down != "up":
                x_new = 0
                y_new = 10
                last_down = "down"
    snake_headx_pos = snake_headx_pos + x_new
    snake_heady_pos = snake_heady_pos + y_new
    dis.fill(field)
    pygame.draw.rect(dis, food, [food_x_pos, food_y_pos, 30, 30])
    pygame.draw.rect(dis, snake, [snake_headx_pos, snake_heady_pos, 30, 30])
    pygame.draw.rect(dis, poison, [poison_y_pos, poison_y_pos, 30, 30])
    snake_Head = []
    snake_Head.append(snake_headx_pos)
    snake_Head.append(snake_heady_pos)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True

    our_snake(snake_blok, snake_List)
    if snake_headx_pos >= width or snake_headx_pos < 0 or snake_heady_pos >= height or snake_heady_pos < 0:
        game_over = True
    if snake_headx_pos == poison_x_pos and snake_heady_pos == poison_y_pos:
        game_over = True
    if snake_headx_pos == food_x_pos and snake_heady_pos == food_y_pos:
        food_x_pos = round(random.randint(0, width - snake_blok) / 10.0) * 10.0
        food_y_pos = round(random.randint(0, height - snake_blok) / 10.0) * 10.0
        score = score+1
        snake_speed = snake_speed+1
        Length_of_snake = Length_of_snake + 1
    user_score(score)
    pygame.display.update()
    fps.tick(snake_speed)

gameOvermsg("Вы проиграли!!!", messageFall)
pygame.display.update()
time.sleep(3)
pygame.quit()
quit()
