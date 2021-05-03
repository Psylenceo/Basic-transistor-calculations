#tkinter to make a window and shorten the name
import tkinter as tk
from tkinter import ttk
#glob allows searching in folders for a file
import glob
#need som maths
import math

#create the app window
root = tk.Tk()
root.title("Transistor Basics")
root.configure(bg = 'black')
#root.geometry("275x100")
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

###############################################################################
#create list of models
CC = tk.Label(master = root, text = "Known transistor models")
CC.grid(row = 0, column = 0, sticky = tk.NSEW, padx = 2, pady = 2)

Models = tk.Listbox(master = root, selectmode = "BROWSE")
Models.grid(row = 1, column = 0, sticky = tk.NSEW, padx = 2, pady = 2)

#create the buttons for T1 selection
T1sel = 0
def CCsel():
    T1sel = 0
    CC.config(bg = 'gainsboro',relief = 'sunken')
    CFG.config(bg = 'white smoke',relief = 'raised')
    
def FCsel():
    T1sel = 1
    CFG.config(bg = 'gainsboro',relief = 'sunken')
    CC.config(bg = 'white smoke',relief = 'raised')
    
    
CC = tk.Button(master = root, text = "Characteristic Curves", command = CCsel, bg = 'gainsboro',relief = 'sunken')
CC.grid(row = 0, column = 1, sticky = tk.NSEW, padx = 2, pady = 2)

CFG = tk.Button(master = root, text = "Follower Configurations", command = FCsel,  bg = 'white smoke',relief = 'raised')
CFG.grid(row = 0, column = 2, sticky = tk.NSEW, padx = 2, pady = 2)

##################################################################################
#create the frame for T2, types of transistors
T2 = tk.Frame(master = root, relief = "groove",bg = 'blue')
T2.grid(row = 1, column = 1, columnspan = 2, sticky = tk.NSEW, padx = 2, pady = 2)

#prameters

#formulas

#create teh buttons for T2
BJT = tk.Button(master = T2, text = "BJT")
BJT.grid(row = 0, column = 0, sticky = tk.NSEW, padx = 2, pady = 2)

FET = tk.Button(master = T2, text = "FET")
FET.grid(row = 0, column = 1, sticky = tk.NSEW, padx = 2, pady = 2)

IGBT = tk.Button(master = T2, text = "IGBT")
IGBT.grid(row = 0, column = 2, sticky = tk.NSEW, padx = 2, pady = 2)
##################################################################################

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.maxsize(root.winfo_width(), root.winfo_height())

root.mainloop() 

