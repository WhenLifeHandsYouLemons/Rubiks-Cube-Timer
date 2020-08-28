"""
high level support for doing this and that
"""
import time
import pygame
pygame.init()

#This sets the size of the window.
WIN = pygame.display.set_mode((1250, 680))
pygame.display.set_caption("Rubik's Cube Timer")

bgColor = 0, 0, 0

timer_start = 0
if timer_start == 0:
    startTime = time.time()
    timer_start = 1

waiting_time = 0

timer_button_x = 700
timer_button_y = 450
timer_button_height = 100
timer_button_width = 250
timer_button_colour = 255, 255, 255

timer_display_font = 'C:/Windows/Fonts/Arial.ttf'
timer_display_size = 150
timer_display_fg = 255, 255, 255
timer_display_bg = None
timer_display_x = timer_button_x - timer_button_x / 10
timer_display_y = 200


def timer_function():
    timer_font = pygame.font.Font(timer_display_font, timer_display_size)
    total_time = str(round(time.time() - startTime, 2))
    timer_display = timer_font.render(total_time, True, timer_display_fg, timer_display_bg)
    textRect = timer_display.get_rect()
    textRect.left = timer_display_x
    textRect.top = timer_display_y
    WIN.blit(timer_display, textRect)

def start_timer():
    pygame.draw.rect(WIN, (timer_button_colour), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

clock = pygame.time.Clock()

def game_window_style():
    WIN.fill(bgColor)
    pygame.draw.rect(WIN, (200, 200, 200), (0, 0, 1250, timer_button_height))
    #d


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
