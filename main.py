import pyautogui
from tkinter import *
from tkinter import messagebox
import time

print("Licensed under the GNU General Purpose License (GPL)")

root = Tk()
root.geometry("300x300")
root.title("Fuck you DiscordAtter")




sussy = messagebox.showinfo('GPL License', "Licensed under the GNU General Purpose License (GPL)")
root.attributes('-topmost', True)


bitch = Label(root, text="Enter users @").pack()
bitchtxt = StringVar()
biccy = Entry(root, textvariable=bitchtxt).pack()


def faggio():
    time.sleep(2)
    ninja = bitchtxt.get()
    while True:
        pyautogui.typewrite(str(ninja))
        time.sleep(0.5)
        pyautogui.press("Enter")
        time.sleep(0.5)
        pyautogui.press("Enter")
        time.sleep(0.5)
        root.mainloop()

def close():
    exit()


faggot = Button(root, text="Start dat bitch", command = faggio).pack()

faggioo = Button(root, text="Stop", command = close).pack()



root.mainloop()
