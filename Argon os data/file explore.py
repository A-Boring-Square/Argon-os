from tkinter import *
from tkinter import filedialog
import os
import keyboard
keyboard.press('f11')
print("""
 ██        ██ ███████ ██       █████   █████  ███    ███ ███████   ████████  █████
 ██   ██   ██ ██      ██      ██   ██ ██   ██ ████  ████ ██           ██    ██   ██
  ██ ████ ██  █████   ██      ██      ██   ██ ██ ████ ██ █████        ██    ██   ██
  ████  ████  ██      ██      ██   ██ ██   ██ ██  ██  ██ ██           ██    ██   ██
  ██      ██  ███████ ███████  █████   █████  ██      ██ ███████      ██     █████


  █████  ██████   ██████   █████  ███   ██      █████   ██████
 ██   ██ ██   ██ ██       ██   ██ ████  ██     ██   ██ ██
 ███████ ██████  ██   ██  ██   ██ ██ ██ ██     ██   ██  █████
 ██   ██ ██   ██ ██    ██ ██   ██ ██  ████     ██   ██      ██
 ██   ██ ██   ██  ██████   █████  ██   ███      █████  ██████   ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴘʏᴛʜᴏɴ
""")
print(" ")
print("press enter to open the file explorer")


def openFile():
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    os.startfile(filepath)

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()