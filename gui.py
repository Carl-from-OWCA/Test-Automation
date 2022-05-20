from ctypes import alignment
from mimetypes import common_types
import config
from app import runTests
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from functools import partial


# Helper Functions =============================================================

def queryFile(var: str) -> None:
    selected = filedialog.askopenfilename(initialdir="/", title="Select a file")
    setattr(config, var, selected)

def queryFolder(var: str) -> None:
    selected = filedialog.askdirectory(initialdir="/", title="Select a folder")
    setattr(config, var, selected)

# End of functions =============================================================


# Start of GUI specification
root = Tk()
root.title("Test Automator")
root.geometry("600x600") # 1920x1080 is full screen
root.resizable(False, False)

frm = ttk.Frame(root, padding=10)
frm.grid()

# Labels
label_exec = ttk.Label(frm, text=config.label_exec, padding=config.default_pad).grid(column=0, row=1, sticky='w')
ttk.Label(frm, text="").grid(column=0, row=2)   # spacer
label_indir = ttk.Label(frm, text=config.label_indir, padding=config.default_pad).grid(column=0, row=3, sticky='w')
label_inext = ttk.Label(frm, text=config.label_inext, padding=config.default_pad).grid(column=0, row=4, sticky='w')
ttk.Label(frm, text="").grid(column=0, row=5)   # spacer
label_outdir = ttk.Label(frm, text=config.label_outdir, padding=config.default_pad).grid(column=0, row=6, sticky='w')
label_outext = ttk.Label(frm, text=config.label_outext, padding=config.default_pad).grid(column=0, row=7, sticky='w')

# Entries

# Buttons
but_exec = ttk.Button(frm, text="Browse", command=partial(queryFile, "program_name")).grid(column=2, row=1)
but_indir = ttk.Button(frm, text="Browse", command=partial(queryFolder, "input_folder")).grid(column=2, row=3)
but_outdir = ttk.Button(frm, text="Browse", command=partial(queryFolder, "output_folder")).grid(column=2, row=6)
but_run = ttk.Button(frm, text="Run Tests", command=runTests).grid(column=1, row=9)

# End of GUI specification =====================================================

root.mainloop()

