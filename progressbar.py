from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import time
root = Tk()

root.geometry("500x500")
root.title("A progress bar")

progress = Progressbar(root, orient=HORIZONTAL, length=300)
def bar():
    progress["value"] = 20
    root.update_idletasks()
    time.sleep(2)

    progress["value"] = 40
    root.update_idletasks()
    time.sleep(2)

    progress["value"] = 50
    root.update_idletasks()
    time.sleep(2)

    progress["value"] = 70
    root.update_idletasks()
    time.sleep(2)

    progress["value"] = 85
    root.update_idletasks()
    time.sleep(2)

    progress["value"] = 100
progress.pack()

Button(root, text = "Start", command=bar).pack()

root.mainloop()