import shutil
import os
import time
print("")

current_file_path = str(os.path.realpath(__file__))

try:
    shutil.rmtree("C:/Rubik's Cube Timer")
    print("The application has been uninstalled, please delete the Rubik's Cube Timer v12.exe file.")
    print("")
    time.sleep(2.5)
    input("Press the 'enter' key to finish uninstalling the application. ")
    os.remove(current_file_path)
except FileNotFoundError:
    print("The application is already uninstalled, please delete the Rubik's Cube Timer.exe file.")
    print("")
    time.sleep(2.5)
    input("Press the 'enter' key to finish uninstalling the application. ")
except:
    print("")
    print("------------------------------")
    print("Error")
    print("")
    print("Unable to remove files for application.")
    print("Please contact developer.")
    time.sleep(2.5)
    input("Press the enter key to exit setup: ")