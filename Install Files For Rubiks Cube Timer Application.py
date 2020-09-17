import os
import time
current_file_path = str(os.path.realpath(__file__))

try:
    os.makedirs("C:/Rubik's Cube Timer/Sessions")
except WindowsError:
    print((""))
    print("Already exists!")

try:
    os.mkdir("C:/Rubik's Cube Timer/Averages")
except WindowsError:
    print("Already exists!")

try:
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
    os.remove(current_file_path)
except:
    print("")
    print("------------------------------")
    print("Error")
    print("")
    print("Unable to create necessary files for application.")
    print("Please contact developer.")

    time.sleep(2.5)
    
    input("Press the enter key to exit setup: ")