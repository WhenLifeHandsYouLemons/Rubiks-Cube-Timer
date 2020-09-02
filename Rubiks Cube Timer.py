"""
high level support for doing this and that
"""
import sys
import os
import time
import pygame
pygame.init()

def get_true_filename(filename):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, filename)


window_height = 680
window_width = 1250
#This sets the size of the window.
WIN = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rubik's Cube Timer")

bgColor = 0, 0, 0

time_start = [0]
start_time = 0
time_taken = ["0.000"]
all_times = []
time_to_average = []

with open(get_true_filename("C:/Users/2005s/Documents/Visual Studio Code/Pygame/Rubiks-Cube-Timer/Session1.txt"), "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        print(line)
        all_times.append(line)
        print(all_times)

line_no = 0
current_ao5 = ""

timer_button_x = 700
timer_button_y = 450
timer_button_height = 100
timer_button_width = 250
timer_button_colour = 255, 255, 255
timer_button_colour_selected = 150, 150, 150
start_display_size = 60
start_display_x = timer_button_x + (timer_button_width // 2)
start_display_y = timer_button_y + (timer_button_height // 2)
start_fg = 0, 0, 0

start_timer_check = [0]

help_size = 24

timer_display_font = "C:/Windows/Fonts/Arial.ttf"
timer_display_size = 150
timer_display_fg = 255, 255, 255
timer_display_bg = None
timer_display_x = timer_button_x - timer_button_x / 10
timer_display_y = 200

title_box_bg = 30, 30, 30
title_bg = None
title_cube_timer_fg = 170, 170, 170
title_b_fg = 60, 60, 255
title_s_fg = 220, 0, 0
title_u_fg = 255, 255, 255
title_i_fg = 255, 140, 0
title_R_fg = 0, 200, 0
title_k_fg = 255, 255, 0
title_display_R_x = (window_width // 18) * 1
title_display_R_y = timer_button_height // 2
title_display_u_x = (window_width // 18) * 2
title_display_u_y = timer_button_height // 2
title_display_b_x = (window_width // 18) * 3
title_display_b_y = timer_button_height // 2
title_display_i_x = (window_width // 18) * 4
title_display_i_y = timer_button_height // 2
title_display_k_x =(window_width // 18) * 5
title_display_k_y = timer_button_height // 2
title_display_apostrophe_x = (window_width // 18) * 6
title_display_apostrophe_y = timer_button_height // 2
title_display_s_x = (window_width // 18) * 7
title_display_s_y = timer_button_height // 2
title_display_cube_timer_x = (window_width // 18) * (25 / 2)
title_display_cube_timer_y = timer_button_height // 2
title_size = 80
title_display_font = "C:/Users/2005s/Documents/Fonts/joystix.ttf"
stats_width = timer_button_x - (window_width - (timer_button_width + timer_button_x))
stats_bg = 150, 150, 150


def timer_function():
    while start_timer_check[0] == 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

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
            start_timer_check.append(0)
            start_timer_check.remove(1)
        
            time_start.append(0)
            time_start.remove(1)
            time_taken.clear()
        
            total_time = float(total_time)
            time_to_average.append(total_time)
            if total_time > 60:
                total_minutes = round(total_time // 60, None)
                total_seconds = round(total_time - (60 * total_minutes), 3)
                if total_seconds >= 10:
                    total_time = (f"{total_minutes}:{total_seconds}")
                else:
                    total_time = (f"{total_minutes}:0{total_seconds}")
            total_time = str(total_time)
            time_taken.append(total_time)

            all_times.append(total_time)
            add_to_file = "\n".join(all_times)
            with open("C:/Users/2005s/Documents/Visual Studio Code/Pygame/Rubiks-Cube-Timer/Session1.txt", "w") as f:
                    f.write(add_to_file)

#        if mouse[0] > timer_button_x and mouse[0] < timer_button_x + timer_button_width and mouse[1] > timer_button_y and mouse[1] < timer_button_y + timer_button_height and pygame.mouse.get_pressed()[0]:
#            start_timer_check.append(0)
#            start_timer_check.remove(1)

#            time_start.append(0)
#            time_start.remove(1)

#            time_taken.clear()
#            time_taken.append(total_time)


def start_timer():
    if start_timer_check[0] == 1:
        timer_function()

    elif keys[pygame.K_RALT] or keys[pygame.K_LALT] or keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL] and start_timer_check[0] == 0:
        start_timer_check.append(1)
        start_timer_check.remove(0)

        start_time = time.time()

        timer_function()

    elif mouse[0] > timer_button_x and mouse[0] < timer_button_x + timer_button_width and mouse[1] > timer_button_y and mouse[1] < timer_button_y + timer_button_height and pygame.mouse.get_pressed()[0] and start_timer_check[0] == 0:
        pygame.draw.rect(WIN, (timer_button_colour_selected), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

        start_timer_check.append(1)
        start_timer_check.remove(0)

        start_time = time.time()

        timer_function()

    else:
        timer_font = pygame.font.Font(timer_display_font, timer_display_size)
        timer_display = timer_font.render(time_taken[0], True, timer_display_fg, timer_display_bg)
        textRect = timer_display.get_rect()
        textRect.left = timer_display_x
        textRect.top = timer_display_y
        WIN.blit(timer_display, textRect)

        pygame.draw.rect(WIN, (timer_button_colour), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

        start_font = pygame.font.Font(title_display_font, start_display_size)
        start_display = start_font.render("Start", True, start_fg, timer_display_bg)
        textRect10 = start_display.get_rect()
        textRect10.center = (start_display_x, start_display_y)
        WIN.blit(start_display, textRect10)

clock = pygame.time.Clock()

def title():
    title_font = pygame.font.Font(title_display_font, title_size)
    title_display_R = title_font.render("R", True, title_R_fg, title_bg)
    title_display_u = title_font.render("u", True, title_u_fg, title_bg)
    title_display_b = title_font.render("b", True, title_b_fg, title_bg)
    title_display_i = title_font.render("i", True, title_i_fg, title_bg)
    title_display_k = title_font.render("k", True, title_k_fg, title_bg)
    title_display_apostrophe = title_font.render("'", True, title_cube_timer_fg, title_bg)
    title_display_s = title_font.render("s", True, title_s_fg, title_bg)
    title_display_cube_timer = title_font.render(" Cube Timer", True, title_cube_timer_fg, title_bg)
    textRect1 = title_display_R.get_rect()
    textRect2 = title_display_u.get_rect()
    textRect3 = title_display_b.get_rect()
    textRect4 = title_display_i.get_rect()
    textRect5 = title_display_k.get_rect()
    textRect6 = title_display_apostrophe.get_rect()
    textRect7 = title_display_s.get_rect()
    textRect8 = title_display_cube_timer.get_rect()
    textRect1.center = (title_display_R_x, title_display_R_y)
    textRect2.center = (title_display_u_x, title_display_u_y)
    textRect3.center = (title_display_b_x, title_display_b_y)
    textRect4.center = (title_display_i_x, title_display_i_y)
    textRect5.center = (title_display_k_x, title_display_k_y)
    textRect6.center = (title_display_apostrophe_x, title_display_apostrophe_y)
    textRect7.center = (title_display_s_x, title_display_s_y)
    textRect8.center = (title_display_cube_timer_x, title_display_cube_timer_y)
    WIN.blit(title_display_R, textRect1)
    WIN.blit(title_display_u, textRect2)
    WIN.blit(title_display_b, textRect3)
    WIN.blit(title_display_i, textRect4)
    WIN.blit(title_display_k, textRect5)
    WIN.blit(title_display_apostrophe, textRect6)
    WIN.blit(title_display_s, textRect7)
    WIN.blit(title_display_cube_timer, textRect8)

def stats():
    #write code for stats here
    print("Hello")

def game_window_style():
    WIN.fill(bgColor)

    pygame.draw.rect(WIN, (stats_bg), (0, 0, stats_width, window_height))
    pygame.draw.rect(WIN, (title_box_bg), (0, 0, window_width, timer_button_height))

    help_font = pygame.font.Font(timer_display_font, help_size)
    help_display = help_font.render("Press 'alt' to start, press 'space' to stop", True, timer_display_fg, timer_display_bg)
    textRect9 = help_display.get_rect()
    textRect9.bottomright = (window_width, window_height)
    WIN.blit(help_display, textRect9)

    averages_display_font = pygame.font.Font(timer_display_font, help_size)
    averages_display = averages_display_font.render("Statistics", True, timer_display_fg, timer_display_bg)
    textRect11 = averages_display.get_rect()
    textRect11.center = (100, 100)
    WIN.blit(averages_display, textRect11)
    if len(time_to_average) >= 5:
        current_ao5 = round((float(time_to_average[-1]) + float(time_to_average[-2]) + float(time_to_average[-3]) + float(time_to_average[-4]) + float(time_to_average[-5])) / 5, 3)
        if current_ao5 >= 60:
            ao5_minutes = round(current_ao5 // 60, None)
            ao5_seconds = round(current_ao5 - (60 * ao5_minutes), 3)
            current_ao5 = f"{ao5_minutes}:{ao5_seconds}"
        current_ao5 = str(current_ao5)
    else:
        current_ao5 = ""
    averages_display = averages_display_font.render(f"Current average of 5: {current_ao5}", True, timer_display_fg, timer_display_bg)
    textRect12 = averages_display.get_rect()
    textRect12.center = (200, 200)
    WIN.blit(averages_display, textRect12)



    stats()
    title()


RUNNING_WINDOW = True

while RUNNING_WINDOW:
    clock.tick(30)

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
