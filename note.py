# coding: shift_jis
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from datetime import datetime
def filereset():
    global file
    file=""
def fileset(ff):
    global file
    file = ff
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
        filename = file
    else :
        filen = fd.asksaveasfilename()
        filename =filen
        if filen :
            with open(filen,"w") as f:
                datafile = open(filen,"w")
    test = input_box.get(0.,tk.END)
    datafile.write(test)
    datafile.close()
    dt_now = datetime.now().replace(microsecond=0)
    statusbar.configure(state="normal")
    statusbar.delete(0, tk.END)
    statusbar.insert(0,str(dt_now)+",noted")
    statusbar.configure(state="readonly")
    messagebox.showinfo("alert","noted")
    fileset(filename)
app = tk.Tk()
app.title("Note")
app.geometry("300x450")
menu = tk.Menu(app)
app.config(menu=menu)
subMenu = tk.Menu(menu)
menu.add_cascade(label="file",menu=subMenu)
subMenu.add_command(label="Open file",command= openfile)
subMenu.add_command(label="New file",command = newfile)
subMenu.add_command(label="Save",command = note)
input_box = tk.Text()
input_box.place(x = 0, y = 0,height= 60,relwidth=1.0)
input_box.pack(side=tk.TOP,fill=tk.X)
run_button = tk.Button(app, text = "note",width=5,command = note)
run_button.place(x=0,relwidth=1.0)
run_button.pack(fill=tk.X)
statusbar = tk.Entry(app)
statusbar.configure(state="readonly")
statusbar.pack(side=tk.BOTTOM,fill=tk.X)
app.mainloop()
