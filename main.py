import os
import shutil
import tkinter as tk
from tkinter import filedialog

def browse_path():
    path = filedialog.askdirectory()
    if path:
        path_entry.delete(0, tk.END)
        path_entry.insert(tk.END, path)
        return path

def organize_file(path_entry):
    path = path_entry.get()


root = tk.Tk()

icon = tk.PhotoImage(file='./assets/icon.png')
bg = tk.PhotoImage(file='./assets/background.png')
logoname = tk.PhotoImage(file='./assets/logoname.png')
logoimage = tk.PhotoImage(file='./assets/logoimage.png')

root.title("Filio")
root.iconphoto(False, icon)

root.geometry("500x500")
root.resizable(False, False)

background = tk.Label(root, image=bg)
background.pack()

logoa = tk.Label(root, image=logoname, bg='#ffff00')
logoa.place(x=20, y=20)
logob = tk.Label(root, image=logoimage, bg='#ffff00')
logob.place(x=60, y=120)

addtext = tk.Label(root, text="Add Path or Browse the Folder:", font=('Cambria', 10), bg='#ffff00')
addtext.place(x=20, y=270)

path_entry = tk.Entry(root, width=65)
path_entry.place(x=20, y=300)

browse_button = tk.Button(root, text="Browse", command=browse_path, height=1)
browse_button.place(x=430, y=300)

organize_button = tk.Button(root, text="Organize", command=lambda:organize_file(path_entry), height=1)
organize_button.place(x=220, y=450)

root.mainloop()
