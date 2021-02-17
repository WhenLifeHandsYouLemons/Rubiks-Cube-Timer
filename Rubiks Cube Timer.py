"""
Made By: Sooraj Sannabhadti
GitHub - https://github.com/WhenLifeHandsYouLemons
Twitter - https://twitter.com/LemonsHandYou
Instagram - https://www.instagram.com/whenlifehandsyoulemons1/
"""

"""
WARNING!
This app works on machines that have Windows Vista and above installed only.
"""

"""
Imports
"""
import sys
import os
import time
import pygame
import random
import shutil
from pygame.locals import *
pygame.init()

print("")

"""
File searching used when in '.exe' format
"""
def get_true_filename(filename):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")
    return os.path.join(base, filename)

"""
App files installer
"""
confirm_uninstall = [0]
def installing_procedure():
    print("The app is not installed!")
    print("")
    total, used, free = shutil.disk_usage("/")
    print("Total space available: %d megabytes" % (free / 1044923))
    print("Total space needed: 5 bytes")
    free_space = (free / 1044923) * 1024
    if free_space >= 5:
        print("")
        i = input("Do you want to install 'Rubik's Cube Timer'? Enter 'Yes' to continue or press to enter key to exit: ")
        if i == "Yes":
            try:
                try:
                    os.makedirs("C:/Rubik's Cube Timer/Sessions")
                except WindowsError:
                    print("")
                    print("Already exists!")
                try:
                    os.mkdir("C:/Rubik's Cube Timer/Sessions/Session 1")
                except WindowsError:
                    print("Already exists!")
                if not os.path.exists("C:/Rubik's Cube Timer/Settings.txt"):
                    open("C:/Rubik's Cube Timer/Settings.txt", "w+")
                else:
                    print("Already exists!")
                if not os.path.exists("C:/Rubik's Cube Timer/Sessions/Session 1/ao5.txt"):
                    open("C:/Rubik's Cube Timer/Sessions/Session 1/ao5.txt", "w+")
                else:
                    print("Already exists!")
                if not os.path.exists("C:/Rubik's Cube Timer/Sessions/Session 1/ao12.txt"):
                    open("C:/Rubik's Cube Timer/Sessions/Session 1/ao12.txt", "w+")
                else:
                    print("Already exists!")
                if not os.path.exists("C:/Rubik's Cube Timer/Sessions/Session 1/Times.txt"):
                    open("C:/Rubik's Cube Timer/Sessions/Session 1/Times.txt", "w+")
                else:
                    print("Already exists!")
                if not os.path.exists("C:/Rubik's Cube Timer/Sessions/Session 1/Scrambles.txt"):
                    open("C:/Rubik's Cube Timer/Sessions/Session 1/Scrambles.txt", "w+")
                else:
                    print("Already exists!")
                time.sleep(2.5)
                print("")
                print("------------------------------")
                input("Almost done! Press the enter key to finish setup and start app: ")
                installed = True
                print("Opening app...")
            except:
                print("")
                print("------------------------------")
                print("Error")
                print("")
                print("Unable to create necessary files for application.")
                print("Please contact developer.")
                time.sleep(2.5)
                print("")
                print("------------------------------")
                input("Press the enter key to exit app: ")
                sys.exit()
        else:
            print("")
            print("Closing installer...")
            sys.exit()
    else:
        print("")
        print("More disk space needed! Please free up storage and restart app.")
        input("Press the enter key to exit app: ")
        sys.exit()

def installed_procedure():
    print("The app is installed!")
    print("Opening app...")

def uninstalling_procedure():
    print("")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* IMPORTANT PLEASE READ *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("")
    i = input("Are you really sure you want to uninstall 'Rubik's Cube Timer'? Enter 'Yes' to continue or press to enter key to exit: ")
    if i == "Yes":
        try:
            try:
                shutil.rmtree("C:/Rubik's Cube Timer")
            except FileNotFoundError:
                print("")
                print("Already removed!")
            time.sleep(2)
            print("")
            print("------------------------------")
            input("Almost done! Press the enter key to finish uninstalling: ")
        except:
            print("")
            print("------------------------------")
            print("Error")
            print("")
            print("Unable to remove application files.")
            print("Please contact developer.")
            time.sleep(2)
            input("Press the enter key to exit uninstaller: ")
    elif i == "":
        print("")
    print("Closing uninstaller...")
    time.sleep(1)
    sys.exit()

def saving_procedure():
    print("Please wait, the files are being saved...")
    length_ao5 = 0
    while length_ao5 != len(all_ao5):
        convert = str(all_ao5[length_ao5])
        all_ao5_str.append(convert)
        length_ao5 = length_ao5 + 1

    add_to_file = "\n".join(all_ao5_str)
    with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/ao5.txt", "w") as f:
        f.write(add_to_file)

    length_ao12 = 0
    while length_ao12 != len(all_ao12):
        convert = str(all_ao12[length_ao12])
        all_ao12_str.append(convert)
        length_ao12 = length_ao12 + 1

    add_to_file = "\n".join(all_ao12_str)
    with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/ao12.txt", "w") as f:
        f.write(add_to_file)

    length_settings = 0
    while length_settings != len(settings):
        convert = str(settings[length_settings])
        settings_str.append(convert)
        length_settings = length_settings + 1

    add_to_file = "\n".join(settings_str)
    with open("C:/Rubik's Cube Timer/Settings.txt", "w") as f:
        f.write(add_to_file)

def check_for_files():
    if confirm_uninstall[0] == 1:
        uninstalling_procedure()
    elif os.path.exists("C:/Rubik's Cube Timer/Sessions/Session 1/ao5.txt") and os.path.exists("C:/Rubik's Cube Timer/Sessions/Session 1/ao12.txt") and os.path.exists("C:/Rubik's Cube Timer/Sessions/Session 1/Times.txt") and os.path.exists("C:/Rubik's Cube Timer/Settings.txt") and os.path.exists("C:/Rubik's Cube Timer/Sessions/Session 1/Scrambles.txt"):
        installed_procedure()
    else:
        installing_procedure()

check_for_files()
time.sleep(2)

""""
Import settings for app
"""
settings = []
with open("C:/Rubik's Cube Timer/Settings.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        settings.append(line)

if len(settings) == 0:
    settings.append("1")
    settings.append("Dark")

session_no = settings[0]
theme_type = settings[1]
settings_str = []

"""
App window
"""
window_height = 645
window_width = 1250
WIN = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Rubik's Cube Timer")

if theme_type == "Dark":
    bg_colour = 0, 0, 0
elif theme_type == "Light":
    bg_colour = 255, 255, 255

"""
Scrambler
"""
all_scrambles = []
current_scramble_list = []
current_scramble = ""
all_moves = ["U", "D", "L", "R", "F", "B", "U2", "D2", "L2", "R2", "F2", "B2", "U'", "D'", "L'", "R'", "F'", "B'"]
number_of_scrambler_moves = 20
while number_of_scrambler_moves != 0:
    current_choice = random.choice(all_moves)
    if len(current_scramble_list) != 0:
        while current_choice == current_scramble_list[-1] or current_choice in current_scramble_list[-1] or current_scramble_list[-1] in current_choice or  current_choice == "U'" and current_scramble_list[-1] == "U2" or current_choice == "U2" and current_scramble_list[-1] == "U'" or current_choice == "D'" and current_scramble_list[-1] == "D2" or current_choice == "D2" and current_scramble_list[-1] == "D'" or current_choice == "L'" and current_scramble_list[-1] == "L2" or current_choice == "L2" and current_scramble_list[-1] == "L'" or current_choice == "R'" and current_scramble_list[-1] == "R2" or current_choice == "R2" and current_scramble_list[-1] == "R'" or current_choice == "F'" and current_scramble_list[-1] == "F2" or current_choice == "F2" and current_scramble_list[-1] == "F'" or current_choice == "B'" and current_scramble_list[-1] == "B2" or current_choice == "B2" and current_scramble_list[-1] == "B'":
            current_choice = random.choice(all_moves)
    current_scramble_list.append(current_choice)
    number_of_scrambler_moves = number_of_scrambler_moves - 1

current_scramble = " ".join(current_scramble_list)
# print(f"The current scramble is: {current_scramble}")

"""
Timer
"""
time_start = [0]
start_time = 0
time_taken = ["0.000"]
start_timer_check = [0]

"""
Statistics
"""
all_times = []
times_to_average = []
times_to_mean = []
all_ao5 = []
all_ao5_str = []
all_ao12 = []
all_ao12_str = []
ao5_check = [0]
ao12_check = [0]

"""
Import times and averages
"""
with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/Times.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_times.append(line)
        line = float(line)
        times_to_mean.append(line)

with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/ao5.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        line = float(line)
        all_ao5.append(line)

with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/ao12.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        line = float(line)
        all_ao12.append(line)

"""
Timer start/stop button variables
"""
timer_button_x = 700
timer_button_y = 450
timer_button_height = 100
timer_button_width = 250

if theme_type == "Dark":
    timer_button_colour = 255, 255, 255
    timer_button_colour_selected = 150, 150, 150
elif theme_type == "Light":
    timer_button_colour = 0, 0, 0
    timer_button_colour_selected = 50, 50, 50

start_display_size = 60
start_display_x = timer_button_x + (timer_button_width // 2)
start_display_y = timer_button_y + (timer_button_height // 2)

if theme_type == "Dark":
    start_fg = 0, 0, 0
elif theme_type == "Light":
    start_fg = 255, 255, 255

"""
Statistics display variables
"""
# statistic_display_font = get_true_filename("arialbd.ttf")
statistic_display_font = "C:/Rubiks-Cube-Timer 1/arialbd.ttf"
statistic_display_size = 36

if theme_type == "Dark":
    statistic_text_colour = 0, 0, 0
elif theme_type == "Light":
    statistic_text_colour = 255, 255, 255
best_time_x = 10
best_time_y = 150
worst_time_x = 10
worst_time_y = best_time_y + 30
total_mean_x = 10
total_mean_y = worst_time_y + 30
current_ao5_x = 10
current_ao5_y = total_mean_y + 30
current_ao12_x = 10
current_ao12_y = current_ao5_y + 30
best_ao5_x = 10
best_ao5_y = current_ao12_y + 30
best_ao12_x = 10
best_ao12_y = best_ao5_y + 30

"""
Help text variables
"""
help_size = 24
help_text_margin = 5
help_text_x = window_width - help_text_margin
help_text_y = window_height - help_text_margin

"""
Timer display variables
"""
# timer_display_font = get_true_filename("arial.ttf")
timer_display_font = "C:/Rubiks-Cube-Timer 1/arial.ttf"
timer_display_size = 150

if theme_type == "Dark":
    timer_display_fg = 255, 255, 255
elif theme_type == "Light":
    timer_display_fg = 0, 0, 0

timer_display_bg = None
timer_display_x = int(timer_button_x - timer_button_x / 10)
timer_display_y = 200

"""
Title display variables
"""
if theme_type == "Dark":
    title_box_colour = 30, 30, 30
elif theme_type == "Light":
    title_box_colour = 205, 205, 205

title_bg = None

if theme_type == "Dark":
    title_R_fg = 0, 200, 0
    title_u_fg = 255, 255, 255
    title_b_fg = 60, 60, 255
    title_k_fg = 255, 255, 0
    title_cube_timer_fg = 170, 170, 170
elif theme_type == "Light":
    title_R_fg = 0, 140, 0
    title_u_fg = 90, 90, 90
    title_b_fg = 40, 40, 235
    title_k_fg = 200, 190, 0
    title_cube_timer_fg = 50, 50, 50

title_i_fg = 255, 140, 0
title_s_fg = 220, 0, 0
title_display_R_x = (window_width // 18) * 1
title_display_R_y = timer_button_height // 2
title_display_u_x = (window_width // 18) * 2
title_display_u_y = timer_button_height // 2
title_display_b_x = (window_width // 18) * 3
title_display_b_y = timer_button_height // 2
title_display_i_x = (window_width // 18) * 4
title_display_i_y = timer_button_height // 2
title_display_k_x = (window_width // 18) * 5
title_display_k_y = timer_button_height // 2
title_display_apostrophe_x = (window_width // 18) * 6
title_display_apostrophe_y = timer_button_height // 2
title_display_s_x = (window_width // 18) * 7
title_display_s_y = timer_button_height // 2
title_display_cube_timer_x = int((window_width // 18) * (25 / 2))
title_display_cube_timer_y = timer_button_height // 2
title_size = 80
# title_display_font = get_true_filename("joystix.ttf")
title_display_font = "C:/Rubiks-Cube-Timer 1/joystix.ttf"
stats_width = timer_button_x - (window_width - (timer_button_width + timer_button_x))

if theme_type == "Dark":
    stats_bg = 150, 150, 150
elif theme_type == "Light":
    stats_bg = 50, 50, 50

"""
Options variables
"""
if theme_type == "Dark":
    # option_button_image = pygame.image.load(get_true_filename("Options Light Icon.png"))
    option_button_image = pygame.image.load("C:/Rubiks-Cube-Timer 1/Options Light Icon.png")
    # back_arrow_button_image = pygame.image.load(get_true_filename("Back Arrow Light Icon.png"))
    back_arrow_button_image = pygame.image.load("C:/Rubiks-Cube-Timer 1/Back Arrow Light Icon.png")
elif theme_type == "Light":
    # option_button_image = pygame.image.load(get_true_filename("Options Dark Icon.png"))
    option_button_image = pygame.image.load("C:/Rubiks-Cube-Timer 1/Options Dark Icon.png")
    # back_arrow_button_image = pygame.image.load(get_true_filename("Back Arrow Dark Icon.png"))
    back_arrow_button_image = pygame.image.load("C:/Rubiks-Cube-Timer 1/Back Arrow Dark Icon.png")

back_arrow_button_x = 25
back_arrow_button_y = 30
back_arrow_button_height = 25
back_arrow_button_width = 30
option_button_x = 5
option_button_y = 5
option_button_width = 30
option_button_height = 30
option_buttons_height = 230
option_buttons_width = option_buttons_height
options_save_times_x = 100
options_save_times_y = 125
options_clear_times_x = options_save_times_x
options_clear_times_y = options_save_times_y + option_buttons_height + 25
options_new_session_x = options_save_times_x + option_buttons_width + 100
options_new_session_y = options_save_times_y
options_delete_session_x = options_clear_times_x + option_buttons_width + 100
options_delete_session_y = options_clear_times_y
options_change_theme_x = options_delete_session_x + option_buttons_width + 100
options_change_theme_y = options_delete_session_y
options_uninstall_x = options_new_session_x + option_buttons_width + 100
options_uninstall_y = options_new_session_y


"""
Option confirm box variables
"""
confirm_box_width = 1000
confirm_box_height = 500
confirm_box_x = (window_width // 2) - (confirm_box_width // 2)
confirm_box_y = (window_height // 2) - (confirm_box_height // 2)
cancel_button_x = 150
cancel_button_y = 400
cancel_button_width = 400
cancel_button_height = 150
confirm_button_x = cancel_button_width + cancel_button_x + 150
cancel_text_x = cancel_button_x + (cancel_button_width // 2)
cancel_text_y = cancel_button_y + (cancel_button_height // 2)
confirm_text_x = confirm_button_x + (cancel_button_width // 2)
confirm_text_y = cancel_button_y + (cancel_button_height // 2)
confirm_box_delay = 200

"""
Timing & stop timer function
"""
def timer_function():

    while start_timer_check[0] == 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

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
        #mouse = pygame.mouse.get_pos()

        if keys[pygame.K_SPACE]:
            start_timer_check.append(0)
            start_timer_check.remove(1)

            time_start.append(0)
            time_start.remove(1)
            time_taken.clear()

            all_times.append(total_time)
            add_to_file = "\n".join(all_times)
            with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/Times.txt", "w") as f:
                f.write(add_to_file)

            total_time = float(total_time)
            times_to_average.append(total_time)
            times_to_mean.append(total_time)
            if total_time > 60:
                total_minutes = round(total_time // 60, None)
                total_seconds = round(total_time - (60 * total_minutes), 3)
                if total_seconds >= 10:
                    total_time = (f"{total_minutes}:{total_seconds}")
                else:
                    total_time = (f"{total_minutes}:0{total_seconds}")
            total_time = str(total_time)
            time_taken.append(total_time)
            ao5_check.append(0)
            ao5_check.remove(1)
            ao12_check.append(0)
            ao12_check.remove(1)

"""
Start timer function
"""
def start_timer():
    if start_timer_check[0] == 1:
        timer_function()
    # elif event.type == KEYUP and start_timer_check[0] == 0:
    #     if event.key == K_RALT or event.key == K_LALT and start_timer_check[0] == 0:
    #         start_timer_check.append(1)
    #         start_timer_check.remove(0)

    #         if ao5_check[0] == 0:
    #             ao5_check.remove(0)
    #             ao5_check.append(1)
    #         if ao12_check[0] == 0:
    #             ao12_check.remove(0)
    #             ao12_check.append(1)

    #         start_time = time.time()

    #         timer_function()
    elif keys[pygame.K_RALT] or keys[pygame.K_LALT] and start_timer_check[0] == 0:
        start_timer_check.append(1)
        start_timer_check.remove(0)

        if ao5_check[0] == 0:
            ao5_check.remove(0)
            ao5_check.append(1)
        if ao12_check[0] == 0:
            ao12_check.remove(0)
            ao12_check.append(1)

        timer_function()
    elif mouse[0] > timer_button_x and mouse[0] < timer_button_x + timer_button_width and mouse[1] > timer_button_y and mouse[1] < timer_button_y + timer_button_height and pygame.mouse.get_pressed()[0] and start_timer_check[0] == 0:

        pygame.draw.rect(WIN, (timer_button_colour_selected), (timer_button_x, timer_button_y, timer_button_width, timer_button_height))

        start_timer_check.append(1)
        start_timer_check.remove(0)

        if ao5_check[0] == 0:
            ao5_check.remove(0)
            ao5_check.append(1)
        if ao12_check[0] == 0:
            ao12_check.remove(0)
            ao12_check.append(1)

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

"""
For FPS
"""
clock = pygame.time.Clock()

"""
RUBIK'S CUBE TIMER title design
"""
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

"""
Statistics panel
"""
def stats():
    stats_display_font = pygame.font.Font(statistic_display_font, statistic_display_size)
    stats_display = stats_display_font.render("Statistics", True, statistic_text_colour, timer_display_bg)
    textRect11 = stats_display.get_rect()
    textRect11.center = (stats_width // 2, timer_button_height + 20)
    WIN.blit(stats_display, textRect11)

    if len(times_to_mean) == 0:
        mean = ""
    else:
        mean = round(sum(times_to_mean) / len(times_to_mean), 3)

    if len(times_to_average) >= 5:
        current_ao5_list = []
        current_ao5_list.append(float(times_to_average[-1]))
        current_ao5_list.append(float(times_to_average[-2]))
        current_ao5_list.append(float(times_to_average[-3]))
        current_ao5_list.append(float(times_to_average[-4]))
        current_ao5_list.append(float(times_to_average[-5]))
        current_ao5_list.remove(max(current_ao5_list))
        current_ao5_list.remove(min(current_ao5_list))
        current_ao5 = round((current_ao5_list[0] + current_ao5_list[1] + current_ao5_list[2]) / 3, 3)

        if ao5_check[0] == 0:
            all_ao5.append((current_ao5))
            ao5_check.remove(0)
            ao5_check.append(1)

        if current_ao5 >= 60:
            current_ao5_minutes = round(current_ao5 // 60, None)
            current_ao5_seconds = round(current_ao5 - (60 * current_ao5_minutes), 3)
            current_ao5 = f"{current_ao5_minutes}:{current_ao5_seconds}"

        current_ao5 = str(current_ao5)
    else:
        current_ao5 = ""

    averages_display_font = pygame.font.Font(timer_display_font, help_size)
    current_ao5_display = averages_display_font.render(f"Current average of 5: {current_ao5}", True, statistic_text_colour, timer_display_bg)
    textRect12 = current_ao5_display.get_rect()
    textRect12.topleft = (current_ao5_x, current_ao5_y)
    WIN.blit(current_ao5_display, textRect12)

    if len(all_ao5) >= 1:
        best_ao5 = min(all_ao5)
        if best_ao5 >= 60:
            best_ao5_minutes = round(best_ao5 // 60, None)
            best_ao5_seconds = round(best_ao5 - (60 * best_ao5_minutes), 3)
            best_ao5 = f"{best_ao5_minutes}:{best_ao5_seconds}"
    else:
        best_ao5 = ""

    averages_display_font = pygame.font.Font(timer_display_font, help_size)
    best_ao5_display = averages_display_font.render(f"Best average of 5: {best_ao5}", True, statistic_text_colour, timer_display_bg)
    textRect15 = best_ao5_display.get_rect()
    textRect15.topleft = (best_ao5_x, best_ao5_y)
    WIN.blit(best_ao5_display, textRect15)

    if len(times_to_average) >= 12:
        current_ao12_list = []
        current_ao12_list.append(float(times_to_average[-1]))
        current_ao12_list.append(float(times_to_average[-2]))
        current_ao12_list.append(float(times_to_average[-3]))
        current_ao12_list.append(float(times_to_average[-4]))
        current_ao12_list.append(float(times_to_average[-5]))
        current_ao12_list.append(float(times_to_average[-6]))
        current_ao12_list.append(float(times_to_average[-7]))
        current_ao12_list.append(float(times_to_average[-8]))
        current_ao12_list.append(float(times_to_average[-9]))
        current_ao12_list.append(float(times_to_average[-10]))
        current_ao12_list.append(float(times_to_average[-11]))
        current_ao12_list.append(float(times_to_average[-12]))
        current_ao12_list.remove(max(current_ao12_list))
        current_ao12_list.remove(min(current_ao12_list))
        current_ao12 = round((current_ao12_list[0] + current_ao12_list[1] + current_ao12_list[2] + current_ao12_list[3] + current_ao12_list[4] + current_ao12_list[5] + current_ao12_list[6] + current_ao12_list[7] + current_ao12_list[8] + current_ao12_list[9]) / 10, 3)

        if ao12_check[0] == 0:
            all_ao12.append(current_ao12)
            ao12_check.remove(0)
            ao12_check.append(1)

        if current_ao12 >= 60:
            current_ao12_minutes = round(current_ao12 // 60, None)
            current_ao12_seconds = round(current_ao12 - (60 * current_ao12_minutes), 3)
            current_ao12 = f"{current_ao12_minutes}:{current_ao12_seconds}"
        current_ao12 = str(current_ao12)
    else:
        current_ao12 = ""

    current_ao12_display = averages_display_font.render(f"Current average of 12: {current_ao12}", True, statistic_text_colour, timer_display_bg)
    textRect13 = current_ao12_display.get_rect()
    textRect13.topleft = (current_ao12_x, current_ao12_y)
    WIN.blit(current_ao12_display, textRect13)

    if len(all_ao12) >= 1:
        best_ao12 = min(all_ao12)
        if best_ao12 >= 60:
            best_ao12_minutes = round(best_ao12 // 60, None)
            best_ao12_seconds = round(best_ao12 - (60 * current_ao12_minutes), 3)
            best_ao12 = f"{best_ao12_minutes}:{best_ao12_seconds}"
    else:
        best_ao12 = ""

    averages_display_font = pygame.font.Font(timer_display_font, help_size)
    best_ao12_display = averages_display_font.render(f"Best average of 12: {best_ao12}", True, statistic_text_colour, timer_display_bg)
    textRect16 = best_ao12_display.get_rect()
    textRect16.topleft = (best_ao12_x, best_ao12_y)
    WIN.blit(best_ao12_display, textRect16)

    mean_display = averages_display_font.render(f"Total average: {mean}", True, statistic_text_colour, timer_display_bg)
    textRect14 = mean_display.get_rect()
    textRect14.topleft = (total_mean_x, total_mean_y)
    WIN.blit(mean_display, textRect14)

    if len(times_to_mean) >= 1:
        best_time = min(times_to_mean)
        if best_time >= 60:
            best_time_minutes = round(best_time // 60, None)
            best_time_seconds = round(best_time - (60 * best_time_minutes), 3)
            best_time = f"{best_time_minutes}:{best_time_seconds}"
    else:
        best_time = ""

    best_display_font = pygame.font.Font(timer_display_font, help_size)
    best_time_display = best_display_font.render(f"Best time: {best_time}", True, statistic_text_colour, timer_display_bg)
    textRect20 = best_time_display.get_rect()
    textRect20.topleft = (best_time_x, best_time_y)
    WIN.blit(best_time_display, textRect20)

    if len(times_to_mean) >= 1:
        worst_time = max(times_to_mean)
        if worst_time >= 60:
            worst_time_minutes = round(worst_time // 60, None)
            worst_time_seconds = round(worst_time - (60 * worst_time_minutes), 3)
            worst_time = f"{worst_time_minutes}:{worst_time_seconds}"
    else:
        worst_time = ""

    worst_display_font = pygame.font.Font(timer_display_font, help_size)
    worst_time_display = worst_display_font.render(f"Worst time: {worst_time}", True, statistic_text_colour, timer_display_bg)
    textRect21 = worst_time_display.get_rect()
    textRect21.topleft = (worst_time_x, worst_time_y)
    WIN.blit(worst_time_display, textRect21)

"""
Help text
"""
def help():
    help_font = pygame.font.Font(timer_display_font, help_size)
    help_display = help_font.render("Press 'alt' to start, press 'space' to stop", True, timer_display_fg, timer_display_bg)
    textRect9 = help_display.get_rect()
    textRect9.bottomright = (help_text_x, help_text_y)
    WIN.blit(help_display, textRect9)

"""
Options background for confirmation dialog box
"""
def options_bg():
    WIN.fill(bg_colour)

    pygame.draw.rect(WIN, (stats_bg), (options_clear_times_x, options_clear_times_y, option_buttons_width, option_buttons_height))
    pygame.draw.rect(WIN, (stats_bg), (options_new_session_x, options_new_session_y, option_buttons_width, option_buttons_height))
    pygame.draw.rect(WIN, (stats_bg), (options_save_times_x, options_save_times_y, option_buttons_width, option_buttons_height))
    pygame.draw.rect(WIN, (stats_bg), (options_delete_session_x, options_delete_session_y, option_buttons_width, option_buttons_height))
    pygame.draw.rect(WIN, (stats_bg), (options_change_theme_x, options_change_theme_y, option_buttons_width, option_buttons_height))
    pygame.draw.rect(WIN, (stats_bg), (options_uninstall_x, options_uninstall_y, option_buttons_width, option_buttons_height))

    options_display_font = pygame.font.Font(statistic_display_font, title_size)
    options_display = options_display_font.render("Options", True, timer_display_fg, timer_display_bg)
    textRect17 = options_display.get_rect()
    textRect17.topleft = (75, 0)
    WIN.blit(options_display, textRect17)

    help_font = pygame.font.Font(timer_display_font, help_size)
    help_display = help_font.render("Press 'esc' to go back or click the back arrow", True, timer_display_fg, timer_display_bg)
    textRect9 = help_display.get_rect()
    textRect9.bottomright = (help_text_x, help_text_y)
    WIN.blit(help_display, textRect9)

    WIN.blit(back_arrow_button_image, (back_arrow_button_x, back_arrow_button_y))

    overlay = pygame.Surface((window_width, window_height))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    WIN.blit(overlay, (0, 0))

    if theme_type == "Dark":
        pygame.draw.rect(WIN, (stats_bg), (confirm_box_x, confirm_box_y, confirm_box_width, confirm_box_height))

        pygame.draw.rect(WIN, (title_box_colour), (confirm_button_x, cancel_button_y, cancel_button_width, cancel_button_height))
        pygame.draw.rect(WIN, (title_box_colour), (cancel_button_x, cancel_button_y, cancel_button_width, cancel_button_height))
    elif theme_type == "Light":
        pygame.draw.rect(WIN, (bg_colour), (confirm_box_x, confirm_box_y, confirm_box_width, confirm_box_height))

        pygame.draw.rect(WIN, (timer_button_colour), (confirm_button_x, cancel_button_y, cancel_button_width, cancel_button_height))
        pygame.draw.rect(WIN, (timer_button_colour), (cancel_button_x, cancel_button_y, cancel_button_width, cancel_button_height))

    cancel_font = pygame.font.Font(title_display_font, start_display_size)

    if theme_type == "Dark":
        cancel_display_text = cancel_font.render("Cancel", True, timer_button_colour, title_box_colour)
    elif theme_type == "Light":
        cancel_display_text = cancel_font.render("Cancel", True, start_fg, timer_button_colour)

    textRect18 = cancel_display_text.get_rect()
    textRect18.center = (cancel_text_x, cancel_text_y)
    WIN.blit(cancel_display_text, textRect18)

    confirm_font = pygame.font.Font(title_display_font, start_display_size)

    if theme_type == "Dark":
        confirm_display_text = confirm_font.render("Confirm", True, timer_button_colour, title_box_colour)
    elif theme_type == "Light":
        confirm_display_text = confirm_font.render("Confirm", True, start_fg, timer_button_colour)

    textRect19 = confirm_display_text.get_rect()
    textRect19.center = (confirm_text_x, confirm_text_y)
    WIN.blit(confirm_display_text, textRect19)

"""
Option buttons
"""
def option_buttons():
    """
    Save all times to another file function
    """
    def save_times():
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        pygame.draw.rect(WIN, (stats_bg), (options_save_times_x, options_save_times_y, option_buttons_width, option_buttons_height))

        if  mouse[0] > options_save_times_x and mouse[0] < options_save_times_x + option_buttons_width and mouse[1] > options_save_times_y and mouse[1] < options_save_times_y + option_buttons_height and pygame.mouse.get_pressed()[0]:
            RUNNING_WINDOW = True

            pygame.time.wait(confirm_box_delay)

            while RUNNING_WINDOW:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                keys = pygame.key.get_pressed()
                mouse = pygame.mouse.get_pos()

                options_bg()

                if mouse[0] > cancel_button_x and mouse[0] < cancel_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    RUNNING_WINDOW = False
                    pygame.time.wait(confirm_box_delay)

                if mouse[0] > confirm_button_x and mouse[0] < confirm_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    print("Exported to your C:/ drive.")

                    add_to_file = "\n".join(all_times)
                    with open(f"C:/Rubik's Cube Timer Session {session_no} Times Exported.txt", "w") as f:
                        f.write(add_to_file)

                    add_to_file = "\n".join(all_scrambles)
                    with open(f"C:/Rubik's Cube Timer Session {session_no} Scrambles Exported.txt", "w") as f:
                        f.write(add_to_file)

                    RUNNING_WINDOW = False
                    pygame.time.wait(confirm_box_delay)

                pygame.display.update()

    """
    Delete all times permanently function
    """
    def clear_times():
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        pygame.draw.rect(WIN, (stats_bg), (options_clear_times_x, options_clear_times_y, option_buttons_width, option_buttons_height))

        if  mouse[0] > options_clear_times_x and mouse[0] < options_clear_times_x + option_buttons_width and mouse[1] > options_clear_times_y and mouse[1] < options_clear_times_y + option_buttons_height and pygame.mouse.get_pressed()[0]:
            RUNNING_WINDOW = True

            pygame.time.wait(confirm_box_delay)

            while RUNNING_WINDOW:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                mouse = pygame.mouse.get_pos()
                keys = pygame.key.get_pressed()

                options_bg()

                if mouse[0] > cancel_button_x and mouse[0] < cancel_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    RUNNING_WINDOW = False
                    pygame.time.wait(confirm_box_delay)

                if mouse[0] > confirm_button_x and mouse[0] < confirm_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    print(f"Cleared all your times, ao's and scrambles in Session {session_no}.")
                    with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/Times.txt", "w") as f:
                        f.write("")
                    with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/Scrambles.txt", "w") as f:
                        f.write("")
                    with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/ao5.txt", "w") as f:
                        f.write("")
                    with open(f"C:/Rubik's Cube Timer/Sessions/Session {session_no}/ao12.txt", "w") as f:
                        f.write("")
                    sys.exit()

                pygame.display.update()

    """
    Make a new session function
    """
    def new_session():
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        pygame.draw.rect(WIN, (stats_bg), (options_new_session_x, options_new_session_y, option_buttons_width, option_buttons_height))

        if  mouse[0] > options_new_session_x and mouse[0] < options_new_session_x + option_buttons_width and mouse[1] > options_new_session_y and mouse[1] < options_new_session_y + option_buttons_height and pygame.mouse.get_pressed()[0]:
            RUNNING_WINDOW = True

            pygame.time.wait(confirm_box_delay)

            while RUNNING_WINDOW:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                mouse = pygame.mouse.get_pos()
                keys = pygame.key.get_pressed()

                options_bg()

                if mouse[0] > cancel_button_x and mouse[0] < cancel_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    RUNNING_WINDOW = False
                    pygame.time.wait(confirm_box_delay)

                pygame.display.update()

    """
    Delete a certain or current session function
    """
    def delete_session():
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        pygame.draw.rect(WIN, (stats_bg), (options_delete_session_x, options_delete_session_y, option_buttons_width, option_buttons_height))

        if  mouse[0] > options_delete_session_x and mouse[0] < options_delete_session_x + option_buttons_width and mouse[1] > options_delete_session_y and mouse[1] < options_delete_session_y + option_buttons_height and pygame.mouse.get_pressed()[0]:
            RUNNING_WINDOW = True

            pygame.time.wait(confirm_box_delay)

            while RUNNING_WINDOW:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                mouse = pygame.mouse.get_pos()
                keys = pygame.key.get_pressed()

                options_bg()

                if mouse[0] > cancel_button_x and mouse[0] < cancel_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    RUNNING_WINDOW = False
                    pygame.time.wait(confirm_box_delay)

                pygame.display.update()

    """
    Change theme function
    """
    def change_theme():
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        pygame.draw.rect(WIN, (stats_bg), (options_change_theme_x, options_change_theme_y, option_buttons_width, option_buttons_height))

        if  mouse[0] > options_change_theme_x and mouse[0] < options_change_theme_x + option_buttons_width and mouse[1] > options_change_theme_y and mouse[1] < options_change_theme_y + option_buttons_height and pygame.mouse.get_pressed()[0]:
            RUNNING_WINDOW = True

            pygame.time.wait(confirm_box_delay)

            while RUNNING_WINDOW:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                mouse = pygame.mouse.get_pos()
                keys = pygame.key.get_pressed()

                options_bg()

                if mouse[0] > confirm_button_x and mouse[0] < confirm_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    if settings[1] == "Dark":
                        settings.pop(1)
                        settings.insert(1, "Light")
                    elif settings[1] == "Light":
                        settings.pop(1)
                        settings.insert(1, "Dark")

                    length_settings = 0
                    while length_settings != len(settings):
                        convert = str(settings[length_settings])
                        settings_str.append(convert)
                        length_settings = length_settings + 1

                    add_to_file = "\n".join(settings_str)
                    with open("C:/Rubik's Cube Timer/Settings.txt", "w") as f:
                        f.write(add_to_file)

                    print(f"Changed theme to '{settings[1]}'.")
                    sys.exit()

                if mouse[0] > cancel_button_x and mouse[0] < cancel_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    RUNNING_WINDOW = False
                    pygame.time.wait(confirm_box_delay)

                pygame.display.update()

    """
    Uninstall function
    """
    def uninstall():
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        pygame.draw.rect(WIN, (stats_bg), (options_uninstall_x, options_uninstall_y, option_buttons_width, option_buttons_height))

        if  mouse[0] > options_uninstall_x and mouse[0] < options_uninstall_x + option_buttons_width and mouse[1] > options_uninstall_y and mouse[1] < options_uninstall_y + option_buttons_height and pygame.mouse.get_pressed()[0]:
            RUNNING_WINDOW = True

            pygame.time.wait(confirm_box_delay)

            while RUNNING_WINDOW:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                mouse = pygame.mouse.get_pos()
                keys = pygame.key.get_pressed()

                options_bg()

                if mouse[0] > confirm_button_x and mouse[0] < confirm_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    RUNNING_WINDOW = False
                    confirm_uninstall.pop(0)
                    confirm_uninstall.append(1)
                    pygame.time.wait(confirm_box_delay)

                if mouse[0] > cancel_button_x and mouse[0] < cancel_button_x + cancel_button_width and mouse[1] > cancel_button_y and mouse[1] < cancel_button_y + cancel_button_height and pygame.mouse.get_pressed()[0]:
                    RUNNING_WINDOW = False
                    pygame.time.wait(confirm_box_delay)

                pygame.display.update()

    """
    Run all settings functions
    """
    save_times()
    clear_times()
    new_session()
    delete_session()
    change_theme()
    uninstall()

"""
Options page
"""
def options():
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    WIN.blit(option_button_image, (option_button_x, option_button_y))

    if mouse[0] > option_button_x and mouse[0] < option_button_x + option_button_width and mouse[1] > option_button_y and mouse[1] < option_button_y + option_button_height and pygame.mouse.get_pressed()[0]:

        pygame.time.wait(confirm_box_delay)

        RUNNING_WINDOW = True

        while RUNNING_WINDOW:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            WIN.fill(bg_colour)

            option_buttons()

            options_display_font = pygame.font.Font(statistic_display_font, title_size)
            options_display = options_display_font.render("Options", True, timer_display_fg, timer_display_bg)
            textRect17 = options_display.get_rect()
            textRect17.topleft = (75, 0)
            WIN.blit(options_display, textRect17)

            help_font = pygame.font.Font(timer_display_font, help_size)
            help_display = help_font.render("Press 'esc' to go back or click the back arrow", True, timer_display_fg, timer_display_bg)
            textRect9 = help_display.get_rect()
            textRect9.bottomright = (help_text_x, help_text_y)
            WIN.blit(help_display, textRect9)

            WIN.blit(back_arrow_button_image, (back_arrow_button_x, back_arrow_button_y))

            if keys[pygame.K_ESCAPE]:
                RUNNING_WINDOW = False
            elif mouse[0] > back_arrow_button_x and mouse[0] < back_arrow_button_x + back_arrow_button_width and mouse[1] > back_arrow_button_y and mouse[1] < back_arrow_button_y + back_arrow_button_height and pygame.mouse.get_pressed()[0]:
                RUNNING_WINDOW = False
                pygame.time.wait(confirm_box_delay)

            if confirm_uninstall[0] == 1:
                RUNNING_WINDOW = False

            pygame.display.update()

"""
Game design background and run all design functions
"""
def game_window_style():
    WIN.fill(bg_colour)

    pygame.draw.rect(WIN, (stats_bg), (0, 0, stats_width, window_height))
    pygame.draw.rect(WIN, (title_box_colour), (0, 0, window_width, timer_button_height))

    options()
    help()
    stats()
    title()

"""
Main loop
"""
RUNNING_WINDOW = True

while RUNNING_WINDOW:
    clock.tick(30)

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    start_time = 0

    """
    Get the timer functions started
    """
    game_window_style()
    start_timer()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or confirm_uninstall[0] == 1:
            RUNNING_WINDOW = False
            pygame.quit()
        #if event.type == KEYUP:
            #if event.key == K_SPACE:
                #print("Space bar released")

"""
Write final times and averages to file before closing
"""
print("")
if confirm_uninstall[0] == 1:
    check_for_files()
else:
    saving_procedure()



time.sleep(2)
print("Closing app...")
time.sleep(1)
sys.exit()
