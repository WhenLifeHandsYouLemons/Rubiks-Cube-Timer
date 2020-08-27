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

timer_button_x = 0
timer_button_y = 0
timer_button_height = 100
timer_button_width = 100

def start_timer():
    pygame.draw.rect(WIN, (255, 255, 255), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

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
    pygame.display.update()



pygame.quit()
