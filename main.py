import pyautogui
import time

print("Licensed under the GNU General Purpose License (GPL)")

sus = input("What is the persons @ tag? Enter @everyone or @here for multiple people. ")

print("Open discord and click on the text field")

def go():
    while True:
        pyautogui.typewrite(str(sus))
        time.sleep(0.5)
        pyautogui.press("Enter")
        time.sleep(0.5)
        pyautogui.press("Enter")
        time.sleep(0.5)
        

time.sleep(10)

go()



