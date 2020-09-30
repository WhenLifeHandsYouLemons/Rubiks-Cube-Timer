import os
import shutil
import time
print("")
total, used, free = shutil.disk_usage("/")
print("Total space available: %d megabytes" % (free / 1044923))
print("Total space needed: 5 bytes")
free = (free / 1044923) * 1024
if free >= 5:
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
                os.mkdir("C:/Rubik's Cube Timer/Averages")
            except WindowsError:
                print("Already exists!")
            if not os.path.exists("C:/Rubik's Cube Timer/Settings.txt"):
                open("C:/Rubik's Cube Timer/Settings.txt", "w+")
            else:
                print("Already exists!")
            if not os.path.exists("C:/Rubik's Cube Timer/Averages/ao5.txt"):
                open("C:/Rubik's Cube Timer/Averages/ao5.txt", "w+")
            else:
                print("Already exists!")
            if not os.path.exists("C:/Rubik's Cube Timer/Averages/ao12.txt"):
                open("C:/Rubik's Cube Timer/Averages/ao12.txt", "w+")
            else:
                print("Already exists!")
            if not os.path.exists("C:/Rubik's Cube Timer/Sessions/Session1.txt"):
                open("C:/Rubik's Cube Timer/Sessions/Session1.txt", "w+")
            else:
                print("Already exists!")
            time.sleep(2.5)
            print("")
            print("------------------------------")
            input("Almost done! Press the enter key to finish setup: ")
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
            input("Press the enter key to exit installer: ")
    elif i == "":
        print("")
else:
    print("")
    print("More space disk needed! Please free up storage and restart installer.")
    input("Press the enter key to exit installer: ")