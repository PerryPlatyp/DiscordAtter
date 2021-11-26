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

cracker = Label(root, text="Message #").pack()
fuccywuccy = IntVar()
bicnic = Entry(root, textvariable=fuccywuccy).pack()

susnumero = 0
def faggio():
    time.sleep(2)
    ninja = bitchtxt.get()
    jimin = fuccywuccy.get()
    susnumero = 0
    while susnumero <= jimin:
        
        bitchcccc = ninja
        pyautogui.typewrite(str(bitchcccc))
        time.sleep(0.1)
        pyautogui.press("Enter")
        time.sleep(0.1)
        pyautogui.press("Enter")
        time.sleep(0.2)
        susnumero += 1
        if susnumero >= jimin:
            laogonma = messagebox.showinfo('Done', "Completed sending the messages.")
            susnumero = 0
            break
        else:
            pass
        

        
        
        

def close():
    exit()


faggot = Button(root, text="Start dat bitch", command = faggio).pack()

faggioo = Button(root, text="Stop", command = close).pack()



root.mainloop()
