import os
import shutil

import tkinter as tk

root = tk.Tk()

icon = tk.PhotoImage(file= './assets/icon.png')
bg = tk.PhotoImage(file='./assets/background.png')
logoname = tk.PhotoImage(file='./assets/logo.png')

root.title("Filio")
root.iconphoto(False, icon)

root.geometry("500x500")
root.resizable(False, False)

background = tk.Label(root, image=bg)
background.pack()

logo = tk.Label(root, image=logoname, bg='#ffff00').place(x=20, y=20)

root.mainloop()