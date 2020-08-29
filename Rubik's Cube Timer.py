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

timer_button_x = 700
timer_button_y = 450
timer_button_height = 100
timer_button_width = 250
timer_button_colour = 255, 255, 255
timer_button_colour_selected = 150, 150, 150
button_click_check = [0]
startTime = time.time()

timer_display_font = "C:/Windows/Fonts/Arial.ttf"
timer_display_size = 150
timer_display_fg = 255, 255, 255
timer_display_bg = None
timer_display_x = timer_button_x - timer_button_x / 10
timer_display_y = 200


def timer_function():
#    time.sleep(0.5)
    while button_click_check[0] == 1:
#        if keys[pygame.K_SPACE]:
#            button_click_check.remove(1)
#            button_click_check.append(0)
#        if mouse[0] > timer_button_x and mouse[0] < timer_button_x + timer_button_width and mouse[1] > timer_button_y and mouse[1] < timer_button_y + timer_button_height and pygame.mouse.get_pressed()[0]:
#            button_click_check.remove(1)
#            button_click_check.append(0)
        timer_font = pygame.font.Font(timer_display_font, timer_display_size)
        total_time = str(round(time.time() - startTime, 3))
        timer_display = timer_font.render(total_time, True, timer_display_fg, timer_display_bg)
        textRect = timer_display.get_rect()
        textRect.left = timer_display_x
        textRect.top = timer_display_y
        WIN.blit(timer_display, textRect)
        pygame.display.update()
        game_window_style()

def start_timer():
    if button_click_check[0] == 1:
        timer_function()
    elif keys[pygame.K_SPACE] and button_click_check[0] == 0:
        button_click_check.append(1)
        button_click_check.remove(0)
        startTime = time.time()
        print(button_click_check)
        timer_function()
    elif mouse[0] > timer_button_x and mouse[0] < timer_button_x + timer_button_width and mouse[1] > timer_button_y and mouse[1] < timer_button_y + timer_button_height and pygame.mouse.get_pressed()[0] and button_click_check[0] == 0:
        pygame.draw.rect(WIN, (timer_button_colour_selected), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))
        print("Clicked!")
        button_click_check.append(1)
        button_click_check.remove(0)
        startTime = time.time()
        timer_function()
    else:
        timer_font = pygame.font.Font(timer_display_font, timer_display_size)
        timer_display = timer_font.render("0.000", True, timer_display_fg, timer_display_bg)
        textRect = timer_display.get_rect()
        textRect.left = timer_display_x
        textRect.top = timer_display_y
        WIN.blit(timer_display, textRect)
        pygame.draw.rect(WIN, (timer_button_colour), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

clock = pygame.time.Clock()

def game_window_style():
    WIN.fill(bgColor)
    pygame.draw.rect(WIN, (200, 200, 200), (0, 0, 1250, timer_button_height))
    #d


RUNNING_WINDOW = True

while RUNNING_WINDOW:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    game_window_style()
    start_timer()
    pygame.display.update()



pygame.quit()
