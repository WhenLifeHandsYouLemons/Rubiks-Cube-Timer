import shutil
import time
print("")
i = input("Are you sure you want to uninstall 'Rubik's Cube Timer'? Enter 'Yes' to continue or press to enter key to exit: ")
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