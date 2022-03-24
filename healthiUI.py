
from cgitb import text
from faulthandler import disable
from logging import captureWarnings
from tkinter import *
from typing_extensions import Literal

from setuptools import Command


root = Tk()
root.title("HEALTHi")

e = Entry(root)
e.pack(padx=15, pady=10)
e.insert(0, "Search")

d = Text(root, width=40, height=25, )
d.pack(padx=15)


barCode = Button(root, text="Scan Barcode", padx=40, pady=50, bg="yellow green")

barCode.pack(pady= 10)


root.mainloop()
