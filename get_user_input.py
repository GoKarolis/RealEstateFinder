import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def get_prices():
    min_price = simpledialog.askstring(title="Price",
                                      prompt="What's minimum price?")
    max_price = simpledialog.askstring(title="Price",
                                      prompt="What's maximum price?")
    return min_price, max_price

def get_size():
    min_size = simpledialog.askstring(title="Size",
                                      prompt="What's minimum size?")
    max_size = simpledialog.askstring(title="Size",
                                      prompt="What's maximum size?")
    return min_size, max_size