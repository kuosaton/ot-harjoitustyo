import sys
import os
sys.path.append(os.path.abspath('../')) # lisätään juurikansio src pythonin hakupolkuun luokan Budget hakemista varten
from budget import Budget

from tkinter import Tk

window = Tk()
window.title("TkInter example")
window.mainloop()