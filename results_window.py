from tkinter import Tk
from tkinter import messagebox
import tkinter


def show_domo_results(dict):
    root = Tk()
    t = tkinter.Text(root)
    results_list = []
    for key, value in dict.items():
        temp = [(" \n " * 3) + key + value]
        results_list.append(temp)
    print(results_list)
    for x in results_list:
        t.insert(tkinter.END, x)
    t.pack()
    root.mainloop()


def show_aruodas_results(dict):
    app = Tk()
    t = tkinter.Text(app)
    results_list = []
    for key, value in dict.items():
        temp = [key + value]
        results_list.append(temp)

    print(type(results_list))
    print(results_list)
    for x in results_list:
        t.insert(tkinter.END, x)
    t.pack()
    app.mainloop()


def show_urls():
    top = Tk()
    top.geometry("100x100")
    messagebox.askokcancel(
        "Aruodas", "For more details please go to www.aruodas.lt and www.domoplius.lt"
    )
    top.mainloop()
