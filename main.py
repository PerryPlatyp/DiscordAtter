try:

    # make an app with a gui using tkinter

    import tkinter as tk
    import pyautogui
    from tkinter import messagebox
    import time
    import termcolor



    # create the window
    root = tk.Tk()

    # make the window default size 800x500
    root.geometry("800x500")

    # make it open in the centre of the screen
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))



    # make the background color #2C2F33
    root.configure(background="#2C2F33")


    # make the window always on top
    root.wm_attributes("-topmost", True)



    # make the title of the window be "My App"
    root.title("Disspam")

    # make a text label which is the same as the title be in the top centre of the window
    label = tk.Label(root, text="Discord Spammer", font=("Helvetica", 20), fg="#FFFFFF", bg="#2C2F33")
    label.pack(pady=10)


    # make a label that says "Message to be sent"
    label = tk.Label(root, text="Message to be sent", font=("Helvetica", 12), fg="#FFFFFF", bg="#2C2F33")
    label.pack(pady=10)


    # make a text box that will take in the message to be sent
    text_box = tk.Entry(root, width=50, bg="#23272A", fg="#ffffff", font=("Helvetica", 15))
    text_box.pack(pady=10)

    # make a label that says "Users handle"
    label = tk.Label(root, text="Users handle WITH NUMBERS", font=("Helvetica", 12), fg="#FFFFFF", bg="#2C2F33")
    label.pack(pady=10)

    # make a text box that will take in the users handle
    text_box2 = tk.Entry(root, width=50, bg="#23272A", fg="#ffffff", font=("Helvetica", 15))
    text_box2.pack(pady=10)

    # make a label that says "Number of messages to be sent"
    label = tk.Label(root, text="Number of messages to be sent", font=("Helvetica", 12), fg="#FFFFFF", bg="#2C2F33")
    label.pack(pady=10)

    # make a text box that will take in the number of messages to be sent
    text_box3 = tk.Entry(root, width=50, bg="#23272A", fg="#ffffff", font=("Helvetica", 15))
    text_box3.pack(pady=10)




    def buttonStart():
        # if m.text_box is empty then dont use it
        if text_box.get() == "":
            print("Message is empty")
        # else if text_box2 is empty then dont use it
        elif text_box2.get() == "":
            print("Handle is empty")
        # else if both of them are empty then dont run the function
        elif text_box.get() == "" and text_box2.get() == "":
            print("Both are empty")
        # else if text_box is not empty and text_box2 is empty then just type out text_box 
        elif text_box.get() != "" and text_box2.get() == "":
            print("Message is: " + text_box.get())
        # else if text_box is empty and text_box2 is not empty then just type out text_box2
        elif text_box.get() == "" and text_box2.get() != "":
            print("Handle is: " + text_box2.get())
        # if both of them are not empty then type out both of them with the 2nd one going first
        else:
            print("Message is: " + text_box.get())
            print("Handle is: " + text_box2.get())

        # get the string from text_box3 and convert it to an integer
        number = int(text_box3.get())

        time.sleep(5)

        for i in range(number):
            time.sleep(0.45)
            pyautogui.typewrite(text_box.get())
            # put a space between the words
            pyautogui.press("space")
            pyautogui.typewrite(text_box2.get())
            pyautogui.typewrite(["enter"])

        # when the for loop is done display a label on the window with a yellow highlight saying done that lasts for 5 seconds
        label = tk.Label(root, text="Done", font=("Helvetica", 24), fg="#FFFFFF", bg="#2C2F33")
        label.pack(pady=10)
        label.configure(background="#FFD700")
        label.after(5000, lambda: label.destroy())



        


    # create a button that says "Send"
    button = tk.Button(root, text="Send", font=("Helvetica", 12), fg="#FFFFFF", bg="#23272A", command=buttonStart)
    button.pack(pady=10)








    # mainloop
    root.mainloop()

except Exception as e:
    termcolor.cprint("[!] Error: " + str(e), "red")
    try:
        # use pip to install pyautogui
        import pip
        pip.main(['install', 'pyautogui'])
        # use pip to install termcolor
        pip.main(['install', 'termcolor'])
    except Exception as e:
        termcolor.cprint("[!] Error: " + str(e), "red")
        termcolor.cprint("There was an error whilst automatically installing required modules. Please contact the files creator.", "red")
