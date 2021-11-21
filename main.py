from tkinter import *  # Button, Label, Listbox, Menu, Tk
from tkinter.constants import BOTH, END, LEFT
from typing import Text
import application
import tkinter
import UI


if __name__ == "__main__":

    interface = UI.UI()
    interface.present()
    interface.root.mainloop()
