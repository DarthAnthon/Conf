from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import platform
import argparse

"python conf1.py conf1.py start_script.sh configuration_file.toml"
root = Tk()

args_parser = argparse.ArgumentParser(prog='conf1')
args_parser.add_argument('path_VFS')
args_parser.add_argument('path_script')
args_parser.add_argument('configuration_file')

class Shell:
    def ls(self, args):
        return f"ls, {args}"
    def cd(self, args):
        return f"cd, {args}"

shell = Shell()
args1 = args_parser.parse_args()
commands = ("ls", "cd", "exit")

Conf_file_path = args1.configuration_file
file = open(Conf_file_path)
VFS_path = file.readline()
Start_script_path = file.readline()
file.close()

Script = open(args1.path_script, 'r')
s1 = Script.readlines()
Script.close()


root.title(VFS_path)
root.geometry("600x600")
frm = ttk.Frame(root, padding=10)
frm.pack()

entry = ttk.Entry(width=50)
entry.pack(anchor=NW, padx=0, pady= 0)


listbox = Listbox()
listbox.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox["yscrollcommand"]=scrollbar.set

listbox.insert(tk.END, VFS_path)
listbox.insert(tk.END, Start_script_path)


def show_message(s):
    global listbox
    listbox.insert(tk.END, s)
    if s!="":
        parser = s.split()
        comm = parser[0]
        args = parser[1:]
        if comm not in commands:
            listbox.insert(tk.END, f"Неизвестная команда {comm}")
            return 0
        if comm == "ls":
            listbox.insert(tk.END, shell.ls(args))
        elif comm == "cd":
            listbox.insert(tk.END, shell.cd(args))
        elif comm == "exit":
            return -1          
        return 1

for t in s1:
    flag = show_message(t)
    if flag == 0 or flag == -1:
        break

def enter(event):
    s=entry.get()
    if show_message(s) == -1:
        root.destroy()
    

entry.bind('<Return>', enter)

root.mainloop()


 
