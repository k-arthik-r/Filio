import os
import shutil
import tkinter as tk

root = tk.Tk()

icon = tk.PhotoImage(file= './assets/icon.png')
bg = tk.PhotoImage(file='./assets/background.png')
logoname = tk.PhotoImage(file='./assets/logoname.png')
logoimage = tk.PhotoImage(file='./assets/logoimage.png') 

root.title("Filio")
root.iconphoto(False, icon)

root.geometry("500x500")
root.resizable(False, False)

background = tk.Label(root, image=bg)
background.pack()

logoa = tk.Label(root, image=logoname, bg='#ffff00').place(x=20, y=20)
logob = tk.Label(root, image=logoimage, bg='#ffff00').place(x=60, y=120)

root.mainloop()