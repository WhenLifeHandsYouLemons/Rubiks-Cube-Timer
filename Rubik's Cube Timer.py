"""
high level support for doing this and that
"""
import pygame
import time
pygame.init()

#This sets the size of the window.
WIN = pygame.display.set_mode((1250, 680))
pygame.display.set_caption("Rubik's Cube Timer")

bgColor = 0, 0, 0

waiting_time = 0

timer_button_x = 700
timer_button_y = 450
timer_button_height = 100
timer_button_width = 250
timer_colour = 255, 255, 255

def timer_function():
    startTime = time.time()
    continuous_time = str(time.time() - startTime)
    timer_font = pygame.font.Font('C:/Users/2005s/Documents/Fonts/Sheandy-dqo7.ttf', 32)
    timer_display = timer_font.render(continuous_time, True, (255, 255, 255), (0, 0, 0))
    textRect = timer_display.get_rect()
    textRect.center = (2 // 2, 2 // 2)

def start_timer():
    pygame.draw.rect(WIN, (timer_colour), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

clock = pygame.time.Clock()

def game_window_style():
    WIN.fill(bgColor)


RUNNING_WINDOW = True

while RUNNING_WINDOW:
    clock.tick(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        
        waiting_time = waiting_time + 0.001

    game_window_style()
    start_timer()
    timer_function()
    pygame.display.update()



pygame.quit()
