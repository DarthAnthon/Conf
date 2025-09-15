from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
root = Tk()

class Shell:
    def ls(self, args):
        return f"ls, {args}"
    def cd(self, args):
        return f"cd, {args}"

shell = Shell()
commands = ("ls", "cd", "exit")

VFS = "C:/Users/Anton/Desktop/учёба/конф/пр 1/conf1.py"
root.title(VFS)
root.geometry("600x600")
frm = ttk.Frame(root, padding=10)
frm.pack()

entry = ttk.Entry(width=50)
entry.pack(anchor=NW, padx=0, pady= 0)


listbox = Listbox()
listbox.pack(side=LEFT, fill=BOTH, expand=1)
# сдвигаем скрол на 1 элемент вниз
scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
  
listbox["yscrollcommand"]=scrollbar.set

def show_message(event):
    s=entry.get()
    global listbox
    listbox.insert(tk.END, s)
    parser = s.split()
    comm = parser[0]
    args = parser[1:]
    for i in range(len(args)):
        var = args[i]
        if args[i][0] == '$':
            args[i] = os.getenv(args[i][1:])
            if args[i] is None:
                listbox.insert(tk.END, f"Переменная {var} не найдена")
    if comm not in commands:
        listbox.insert(tk.END, f"Неизвестная команда {comm}")
    if comm == "ls":
        listbox.insert(tk.END, shell.ls(args))
    elif comm == "cd":
        listbox.insert(tk.END, shell.cd(args))
    elif comm == "exit":
        root.destroy()



entry.bind('<Return>', show_message)




root.mainloop()

#ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)

#btn = ttk.Button(text="Click", command=show_message)
#btn.pack(anchor=NW, padx=6, pady=6)
 