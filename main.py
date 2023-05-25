import os
import shutil

import tkinter as tk

root = tk.Tk()

icon = tk.PhotoImage(file= 'icon.png')

root.geometry("500x500")
root.iconphoto(False, icon)
root.title("Filio")


root.mainloop()