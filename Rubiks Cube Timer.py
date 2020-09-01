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

time_start = [0]
start_time = 0
time_taken = ["0.000"]

timer_button_x = 700
timer_button_y = 450
timer_button_height = 100
timer_button_width = 250
timer_button_colour = 255, 255, 255
timer_button_colour_selected = 150, 150, 150

button_click_check = [0]

timer_display_font = "C:/Windows/Fonts/Arial.ttf"
timer_display_size = 150
timer_display_fg = 255, 255, 255
timer_display_bg = None
timer_display_x = timer_button_x - timer_button_x / 10
timer_display_y = 200


def timer_function():
    while button_click_check[0] == 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_WINDOW = False

        if time_start[0] == 0:
            start_time = time.time()
            time_start.append(1)
            time_start.remove(0)
        
        timer_font = pygame.font.Font(timer_display_font, timer_display_size)
        total_time = str(round(time.time() - start_time, 3))
        timer_display = timer_font.render(total_time, True, timer_display_fg, timer_display_bg)
        textRect = timer_display.get_rect()
        textRect.left = timer_display_x
        textRect.top = timer_display_y
        WIN.blit(timer_display, textRect)

        pygame.display.update()
        
        game_window_style()
        
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        if keys[pygame.K_SPACE]:
            button_click_check.append(0)
            button_click_check.remove(1)
        
            time_start.append(0)
            time_start.remove(1)
            time_taken.clear()
        
            total_time = float(total_time)
            if total_time > 60:
                total_minutes = round(total_time // 60, None)
                total_seconds = round(total_time - (60 * total_minutes), 3)
                if total_seconds >= 10:
                    total_time = (f"{total_minutes}:{total_seconds}")
                else:
                    total_time = (f"{total_minutes}:0{total_seconds}")
            total_time = str(total_time)
            time_taken.append(total_time)

#        if mouse[0] > timer_button_x and mouse[0] < timer_button_x + timer_button_width and mouse[1] > timer_button_y and mouse[1] < timer_button_y + timer_button_height and pygame.mouse.get_pressed()[0]:
#            button_click_check.append(0)
#            button_click_check.remove(1)

#            time_start.append(0)
#            time_start.remove(1)

#            time_taken.clear()
#            time_taken.append(total_time)


def start_timer():
    if button_click_check[0] == 1:
        timer_function()

    elif keys[pygame.K_RALT] or keys[pygame.K_LALT] and button_click_check[0] == 0:
        button_click_check.append(1)
        button_click_check.remove(0)

        start_time = time.time()

        timer_function()

#    elif mouse[0] > timer_button_x and mouse[0] < timer_button_x + timer_button_width and mouse[1] > timer_button_y and mouse[1] < timer_button_y + timer_button_height and pygame.mouse.get_pressed()[0] and button_click_check[0] == 0:
#        pygame.draw.rect(WIN, (timer_button_colour_selected), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

#        button_click_check.append(1)
#        button_click_check.remove(0)

#        start_time = time.time()

#        timer_function()

    else:
        timer_font = pygame.font.Font(timer_display_font, timer_display_size)
        timer_display = timer_font.render(time_taken[0], True, timer_display_fg, timer_display_bg)
        textRect = timer_display.get_rect()
        textRect.left = timer_display_x
        textRect.top = timer_display_y
        WIN.blit(timer_display, textRect)

        pygame.draw.rect(WIN, (timer_button_colour), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

clock = pygame.time.Clock()

def game_window_style():
    WIN.fill(bgColor)
    pygame.draw.rect(WIN, (200, 200, 200), (0, 0, 1250, timer_button_height))


RUNNING_WINDOW = True

while RUNNING_WINDOW:
    clock.tick(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    start_time = 0

    game_window_style()
    start_timer()

    pygame.display.update()



pygame.quit()
