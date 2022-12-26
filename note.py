# coding: shift_jis
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import os
from datetime import datetime
setfile= open("settings.txt","w")
setfile.close()
def filereset():
    global file
    file=""
filereset()
def newfile():
    ask1 = messagebox.askokcancel("New file create:","Can I reset textbox value?")
    if ask1 == True :
        input_box.delete(0.,tk.END)
        filereset()
def openfile():
    global file
    file = fd.askopenfilename(
    title = "Choose a file",
    filetypes=[("TEXT", ".txt")])
    if file:
        with open(file, "r", encoding="utf_8") as f:
            text = f.read()
            input_box.delete(0.,tk.END)
            input_box.insert(0.,text)
def note():
    if file != "":
        datafile = open(file,"w")
    else :
        filename = fd.asksaveasfilename()
        if filename :
            with open(filename,"w") as f:
                datafile = f
    test = input_box.get(0.,tk.END)
    datafile.write(test)
    datafile.close()
    dt_now = datetime.now().replace(microsecond=0)
    statusbar.configure(state="normal")
    statusbar.delete(0, tk.END)
    statusbar.insert(0,str(dt_now)+",noted")
    statusbar.configure(state="readonly")
    messagebox.showinfo("alert","noted")
app = tk.Tk()
app.title("Note")
app.geometry("350x100")
menu = tk.Menu(app)
app.config(menu=menu)
subMenu = tk.Menu(menu)
menu.add_cascade(label="file",menu=subMenu)
subMenu.add_command(label="Open file",command= openfile)
subMenu.add_command(label="New file",command = newfile)
subMenu.add_command(label="Save",command = note)
run_button = tk.Button(app, text = "note",width = 2,command = note)
run_button.place(x = 300, y = 5)
input_box = tk.Text(width = 35)
input_box.place(x = 5, y = 10,height= 60)
statusbar = tk.Entry(app, width = 40)
statusbar.configure(state="readonly")
statusbar.place(x = 10, y = 35)
statusbar.pack(side = tk.BOTTOM,fill=tk.X)
app.mainloop()
