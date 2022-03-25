from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("428x926")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 926,
    width = 428,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

window.resizable(False, False)
window.mainloop()
